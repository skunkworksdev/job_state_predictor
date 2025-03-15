# job_state_predictor

The objective of this project is as follows: given the details of a Slurm job at its submission time, determine the state of the job. This is accomplished by an ML approach.

The dataset for this project is Eash, Matthew, and Hilary Egan. 2020. "NREL HPC Eagle Jobs Data." NREL Data Catalog. Golden, CO: National Renewable Energy Laboratory. Last updated: January 21, 2025. DOI: 10.7799/1722950.

The dataset metadata is given below:
 
·  start_time: The date and time the job actually began execution on the compute nodes. This is distinct from when the job was submitted.

·  submit_time: The date and time the job was submitted to the Slurm scheduler. This marks the point when the job entered the queue.

·  end_time: The date and time the job completed execution, either successfully or due to an error.

·  state: The final status of the job. Common states include:

·         COMPLETED: Job finished successfully.

·         FAILED: Job terminated due to an error.

·         CANCELLED: Job was manually cancelled by the user or administrator.

·         TIMEOUT: Job exceeded its allocated walltime.

·         PENDING: Job is waiting in the queue for resources to become available.

·         RUNNING: Job is currently executing on compute nodes.

·         SUSPENDED: Job has been temporarily suspended.

·  qos: The Quality of Service associated with the job. QOS determines resource allocation, priority, and potentially billing. Different QOS levels might have access to different partitions or resource limits.

·  partition: The name of the compute partition the job ran (or was intended to run) on. Partitions are logical groupings of nodes with specific hardware characteristics (e.g., different CPU architectures, GPUs, memory capacity). See https://www.nrel.gov/hpc/assets/pdfs/slurm-new-nrel-capabilities-presentation.pdf

·  nodelist: A list of the specific compute nodes assigned to the job. This helps track where the job ran and can be useful for debugging or performance analysis.

·  processors_req: The number of processors (CPU cores) requested by the job.

·  nodes_req: The number of compute nodes requested by the job.

·  wallclock_req: The requested wall clock time (elapsed time) for the job. This is the maximum time the job is allowed to run before it is terminated. Expressed in hours, minutes, and seconds, or a similar format.

·  wallclock_used: The actual wall clock time used by the job. This is the elapsed time from start_time to end_time.

·  processors_used: The number of processors (CPU cores) actually used by the job. This might be less than processors_req if the job didn't utilize all requested cores.

·  nodes_used: The number of compute nodes actually used by the job. Similar to processors_used, this might be less than nodes_req.

·  queue_wait: The amount of time the job spent in the queue waiting to be scheduled. This is the difference between submit_time and start_time.

·  job_id: The unique identifier assigned to the job by Slurm. This is essential for tracking and managing jobs.

·  account (anonymized): The anonymized account associated with the job. This is used for accounting and resource allocation tracking.

·  script (anonymized): The anonymized name or path of the submission script used to launch the job. This can give clues about the type of workload.

·  user (anonymized): The anonymized username of the user who submitted the job.

·  std_power: The standard deviation of the power consumption of the job. This metric indicates the variability in power usage during the job's execution.

·  avg_power: The average power consumption of the job. This provides a measure of the job's overall energy usage.

·  array_pos: If the job is part of a job array, this field indicates the index or position of the specific job within the array. If the job is not part of an array, this field might be absent or have a null value.

