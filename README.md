# job_state_predictor

The metric collector proposed might be better than existing polling based collector because:
1. With batching, it achieves the same effect as a polling based collector, but with a much smaller set of jobs for which data has to be retrieved.
2. If jobs complete in a very small interval, sstat is avoided.
3. Monitoring jobs per partitions and monitoring nodes all can be done through just one call to Slurmctld, unlike solutions that perform separate calls just for the purpose.
