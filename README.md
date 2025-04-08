# job_state_predictor

The metric collector proposed might be better than existing polling based collector because:
1. With batching, it achieves the same effect as a polling based collector, but with a much smaller set of jobs for which data has to be retrieved.
2. If jobs complete in a very small interval, sstat is avoided.
3. Monitoring jobs per partitions and monitoring nodes all can be done through just one call to Slurmctld, unlike solutions that perform separate calls just for the purpose.

Job State Prediction seems to be impractical because:
1. The scope of Slurm Job failures is very large. Some of the reasons for which jobs fail are:
   1. Low Memory Allocation
   2. Incorrect Permissions
   3. Software incompatible with the hardware.
   4. Improper timeout allocation
   5. Disk quota
   6. Billing
   7. Errors in the code itself
   8. Node Failure
2. If there are plenty of resources in a Slurm cluster, Slurm simply allocates all the resources to a job. When multiple jobs have the same pattern and we try to predict job failure at submission or allocation time just by these parameters, how will the model differentiate the normal jobs from the potential fail jobs?
3. Everything else known(2,3,5,6,7,8), we might require ML to find the estimate the memory or timeout requirements. If one proceeds to trace everything what the program does and uses, the purpose of job state predictor to lessen wastage of resources itself is lost; for each job a very long complex pipeline will have to be followed.

We can do several other things like runtime prediction (which NREL has done, applying XALT for job tracking), power consumption related activities, node failure, resource allocation(?) etc.
   
