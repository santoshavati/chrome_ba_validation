How to use asr_pnp_automation scripts

- copy asr_cmd.sh to DUT path /usr/local/ml_benchmark 
- copy run_asr_eval.py to DUT path /usr/local/ml_benchmark/scripts
- copy asr_pnp_data.py to your host machine
- login to DUT and execute below cmd
	$ cd /usr/local/ml_benchmark
	$ chmod +x asr_cmd.sh
	$ ./asr_cmd.sh 
- the above cmd will generate asr and socwatch csv file.
- copy this csv files to your host machine where asr_pnp_data.py copied
- on your host machine execute 
	$ ./asr_pnp_data.py
- File "kpi_perf.csv: have pnp numbers 
