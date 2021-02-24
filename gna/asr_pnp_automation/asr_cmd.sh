#Encoder 1 on GNA, rest on CPU	
sudo python2 scripts/update_lp_config_symlink.py --source_config=soda/lp_quantized_nnapi/dictation_nnapi_enc1_delegation.config
sudo python2 scripts/run_asr_eval.py --disable_services --audio_files_proto=configs/file_lists/testdata-small-files.ascii_proto --soda_driver_path=libsoda_chromeos_keyless-tigerlake.so --soda_lp_dir=soda/lp_quantized_nnapi --csv_output_path=$PWD/ --dictation_config_name=dictation_nnapi_enc1_delegation.config


#Decoder on GNA ,rest on CPU	
sudo python2 scripts/update_lp_config_symlink.py --source_config=soda/lp_quantized_nnapi/dictation_nnapi_dec_delegation.config
sudo python2 scripts/run_asr_eval.py --disable_services --audio_files_proto=configs/file_lists/testdata-small-files.ascii_proto --soda_driver_path=libsoda_chromeos_keyless-tigerlake.so --soda_lp_dir=soda/lp_quantized_nnapi --csv_output_path=$PWD/ --dictation_config_name=dictation_nnapi_dec_delegation.config



#Decoder and Encoder 0 on GNA, rest on CPU
sudo python2 scripts/update_lp_config_symlink.py --source_config=soda/lp_quantized_nnapi/dictation_nnapi_dec_enc0_delegation.config
sudo python2 scripts/run_asr_eval.py --disable_services --audio_files_proto=configs/file_lists/testdata-small-files.ascii_proto --soda_driver_path=libsoda_chromeos_keyless-tigerlake.so --soda_lp_dir=soda/lp_quantized_nnapi --csv_output_path=$PWD/ --dictation_config_name=dictation_nnapi_dec_enc0_delegation.config

#Decoder and Encoders on GNA, Joint on CPU
sudo python2 scripts/update_lp_config_symlink.py --source_config=soda/lp_quantized_nnapi/dictation_nnapi_dec_enc0_enc1_delegation.config
sudo python2 scripts/run_asr_eval.py --disable_services --audio_files_proto=configs/file_lists/testdata-small-files.ascii_proto --soda_driver_path=libsoda_chromeos_keyless-tigerlake.so --soda_lp_dir=soda/lp_quantized_nnapi --csv_output_path=$PWD/ --dictation_config_name=dictation_nnapi_dec_enc0_enc1_delegation.config

#Encoder 0 on GNA, rest on CPU	
sudo python2 scripts/update_lp_config_symlink.py --source_config=soda/lp_quantized_nnapi/dictation_nnapi_enc0_delegation.config
sudo python2 scripts/run_asr_eval.py --disable_services --audio_files_proto=configs/file_lists/testdata-small-files.ascii_proto --soda_driver_path=libsoda_chromeos_keyless-tigerlake.so --soda_lp_dir=soda/lp_quantized_nnapi --csv_output_path=$PWD/ --dictation_config_name=dictation_nnapi_enc0_delegation.config

#Encoders on GNA, rest on CPU
sudo python2 scripts/update_lp_config_symlink.py --source_config=soda/lp_quantized_nnapi/dictation_nnapi_enc0_enc1_delegation.config
sudo python2 scripts/run_asr_eval.py --disable_services --audio_files_proto=configs/file_lists/testdata-small-files.ascii_proto --soda_driver_path=libsoda_chromeos_keyless-tigerlake.so --soda_lp_dir=soda/lp_quantized_nnapi --csv_output_path=$PWD/ --dictation_config_name=dictation_nnapi_enc0_enc1_delegation.config