#!/usr/bin/python3

import os
import logging
import re
import subprocess

# Configure logging
logging.basicConfig(filename="/var/log/slurm/epilog.log", level=logging.INFO, format="%(asctime)s %(message)s")

slurm_job_logs_location = '/var/log/slurm/slurm_job_logs'
os.makedirs(slurm_job_logs_location, exist_ok=True)

job_id = os.getenv("SLURM_JOB_ID")
logging.info(f"Job {job_id} has been completed.")
nodelist = os.getenv("SLURM_JOB_NODELIST")
logging.info(f"Nodelist={nodelist}")

check = re.findall(r'\[', nodelist)
nodes = []
if check:
    x1 = re.finditer(r'\[', nodelist)
    x2 = re.finditer(r'\]', nodelist)
    c = 0
    for (i,j) in zip(x1,x2):
        if c == 0:
            name_prefix = nodelist[ : i.start()]
            prev_end_bracket = j
        else:
            name_prefix = nodelist[prev_end_bracket.start() + 2 : i.start()]
        node_batch = nodelist[i.start() + 1:j.start()]
        node_sets = node_batch.split(',')
        for node_set in node_sets:
            node_range = node_set.split('-')
            if len(node_range) != 1:
                for node_num in range(int(node_range[0]), int(node_range[1]) + 1):
                    nodes.append(name_prefix+str(node_num))
            else:
                nodes.append(name_prefix+node_set)
        c += 1

else:
    nodes.append(nodelist)

logging.info(f"Actual Hostnames={','.join(nodes)}")
logging.info("Copying job logs from nodes")

for node in nodes:
    stdout_path = os.getenv("SLURM_JOB_STDOUT")
    stderr_path = os.getenv("SLURM_JOB_STDERR")
    result = subprocess.run(['scp', f'{node}:{stdout_path}', f'{slurm_job_logs_location}/{job_id}/{job_id}_output.log'], capture_output=True, text=True)
    if stdout_path != stderr_path and result.returncode == 0:
        subprocess.run(['scp', f'{node}:{stdout_path}', f'{slurm_job_logs_location}/{job_id}/{job_id}_error.log'])
    if result.returncode == 0:
        logging.info(f"Copied job logs from {node} successfully")
    else:
        logging.info(f"Could not copy job logs from {node} due to error:{result.stderr}")

