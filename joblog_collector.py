from flask import Flask, request
import json
import os
import logging
import subprocess

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

slurm_job_logs_location = '/var/log/slurm/slurm_job_logs'
os.makedirs(slurm_job_logs_location, exist_ok=True)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.post('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    job_details = json.loads(request.data.decode('utf-8'))
    job_id = job_details['job_id']
    nodes = job_details['nodes']
    stdout_path = job_details['stdout']
    stderr_path = job_details['stderr']
    if stdout_path == None and stderr_path == None:
        return "Interactive Job"

    logging.info("Copying job logs from nodes")
    os.makedirs(f'{slurm_job_logs_location}/{job_id}')

    for node in nodes:
        if stdout_path:
            result = subprocess.run(['scp', f'{node}:{stdout_path}', f'{slurm_job_logs_location}/{job_id}/{job_id}_output.log'], capture_output=True, text=True)
        if stderr_path and stdout_path != stderr_path and result1.returncode == 0:
            result = subprocess.run(['scp', f'{node}:{stdout_path}', f'{slurm_job_logs_location}/{job_id}/{job_id}_error.log'], capture_output=True, text=True)
        if result.returncode == 0:
            logging.info(f"Copied job logs from {node} successfully")
        else:
            logging.info(f"Could not copy job logs from {node} due to error:{result.stderr}")
    return "Successfully copied logs"



# main driver function
if __name__ == '__main__':
    port = 5010
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(port=port)
