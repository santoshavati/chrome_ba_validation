#!/usr/bin/python
import re
import csv

total_rtf =0.0
avg_rtf = 0.0
number_of_testdata = 0
max_rtf =0
count_rtf_gt_two = 0
two = 2.0
pkg_power = 0.0


def pnp_parse(asr_csv_file, socwatch_csv_file):
    global total_rtf
    global avg_rtf
    global number_of_testdata
    global max_rtf
    global count_rtf_gt_two
    global two
    global pkg_power

    with open(socwatch_csv_file,'r') as file:
        for line in file:
            rtf = re.search('Package Power', line)
            if rtf != None:
                #print(line)
                line = file.next()
                line = file.next()
                line = file.next()
                line = file.next()
                line = file.next()
                line = file.next()
                line = file.next()
                line = file.next()
                #print(line)
                word = re.split(',', line)
                pkg_power = word[2]
                print("Package Power (mW) =" +  (pkg_power))
                break
        file.close

    with open(asr_csv_file,'r' ) as csvfile:
        data = csv.DictReader(csvfile)
        #print("filename     RTF Value")
        #print("---------------------------------")
        for row in data:
            #print(row['filename'], row['rtf'])
            #number_of_testdata = 0
            number_of_testdata += 1
            total_rtf += float(row['speech_rtf'])

            if float(row['speech_rtf']) > (2.0):
                count_rtf_gt_two += 1
            if float(row['speech_rtf']) > max_rtf:
                max_rtf = float(row['speech_rtf'])

        avg_rtf = total_rtf/number_of_testdata
        print("Average RTF = " + str(avg_rtf))
        print("Maximum RTF = " + str(max_rtf))
        print("Count of RTF more then two =" + str(count_rtf_gt_two))


def initialize_variable():
    global total_rtf
    global avg_rtf
    global number_of_testdata
    global max_rtf
    global count_rtf_gt_two
    global two
    global pkg_power


    total_rtf =0.0
    avg_rtf = 0.0
    number_of_testdata = 0
    max_rtf =0
    count_rtf_gt_two = 0
    two = 2.0
    pkg_power = 0.0


with open('kpi_perf.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["workload", "Config", "Average RTF", "Max RTF", "No. RTF > 2", "Package Power(mW)"])

    initialize_variable()
    pnp_parse("asr_dictation_nnapi_enc1_delegation.config", "socwatch_dictation_nnapi_enc1_delegation.config.csv")
    writer.writerow(["Encoder 1 on GNA, rest on CPU", "dictation_nnapi_enc1_delegation.config", avg_rtf, max_rtf, count_rtf_gt_two, float(pkg_power)])

    initialize_variable()
    pnp_parse("asr_dictation_nnapi_dec_delegation.config", "socwatch_dictation_nnapi_dec_delegation.config.csv")
    writer.writerow(["Decoder on GNA ,rest on CPU", "dictation_nnapi_dec_delegation.config.csv", avg_rtf, max_rtf, count_rtf_gt_two, float(pkg_power)])

    initialize_variable()
    pnp_parse("asr_dictation_nnapi_dec_enc0_delegation.config", "socwatch_dictation_nnapi_dec_enc0_delegation.config.csv")
    writer.writerow(["Decoder and Encoder 0 on GNA, rest on CPU", "dictation_nnapi_dec_enc0_delegation.config", avg_rtf, max_rtf, count_rtf_gt_two, float(pkg_power)])


    initialize_variable()
    pnp_parse("asr_dictation_nnapi_dec_enc0_enc1_delegation.config", "socwatch_dictation_nnapi_dec_enc0_enc1_delegation.config.csv")
    writer.writerow(["Decoder and Encoders on GNA, Joint on CPU", "dictation_nnapi_dec_enc0_enc1_delegation.config  ", avg_rtf, max_rtf, count_rtf_gt_two, float(pkg_power)])
 
    initialize_variable()
    pnp_parse("asr_dictation_nnapi_enc0_delegation.config", "socwatch_dictation_nnapi_enc0_delegation.config.csv")
    writer.writerow(["Encoder 0 on GNA, rest on CPU", "dictation_nnapi_enc0_delegation.config", avg_rtf, max_rtf, count_rtf_gt_two, float(pkg_power)])
    
    initialize_variable()
    pnp_parse("asr_dictation_nnapi_enc0_enc1_delegation.config", "socwatch_dictation_nnapi_enc0_enc1_delegation.config.csv")
    writer.writerow(["Encoders on GNA, rest on CPU", "dictation_nnapi_enc0_enc1_delegation.config", avg_rtf, max_rtf, count_rtf_gt_two, float(pkg_power)])
 

    csvfile.close

