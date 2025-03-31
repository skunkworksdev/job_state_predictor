#!/usr/bin/python3

import os
import logging
import re
import subprocess
import json
import urllib.request

# Configure logging
logging.basicConfig(filename="/var/log/slurm/epilog.log", level=logging.INFO, format="%(asctime)s %(message)s")

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

job_dict = {}
job_dict['job_id'] = job_id
job_dict['nodes'] = nodes
job_dict['stdout'] = os.getenv("SLURM_JOB_STDOUT")
job_dict['stderr'] = os.getenv("SLURM_JOB_STDERR")

logging.info(f"Actual Hostnames={','.join(nodes)}")
logging.info("Sending data to Log Collector")

myurl = "http://localhost:5010"

req = urllib.request.Request(myurl)
req.add_header('Content-Type', 'application/json; charset=utf-8')
payload = json.dumps(job_dict).encode('utf-8')
try:
    with urllib.request.urlopen(req, payload) as response:
        logging.info(f"Job Info sent succesfully. {response.read().decode('utf-8')}")
except Exception as e:
    logging.info(f"Data transfer failed. {e}")
