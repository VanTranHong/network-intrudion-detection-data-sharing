#!/bin/bash

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --model_name IF --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2017&

################# We are training on the benign data of 2017 and 2018 and testing the malicious data of 2018

######################## Wednesday 14/02################
# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv Wednesday-14-02-2018/Benignonly.csv --mal_sources Wednesday-14-02-2018/SSH-BruteForceonly.csv --attack_types SSH-BruteForce --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2017 CIC-IDS-2018&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv Wednesday-14-02-2018/Benignonly.csv --mal_sources  Wednesday-14-02-2018/FTP-BruteForceonly.csv --attack_types FTP-BruteForce --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2017 CIC-IDS-2018&


# # # ######################## Thursday 15/02################
# python sup_unsup_run.py --data_rep=nfstream --benign_sources Benign_only.csv --mal_sources labeled.csv --attack_types Malicious --num_agents=1 --model_name KDE --mal_folders CTU-IoT-Malware-Capture-34-1/  --benign_folders CTU-IoT-Malware-Capture-3-1/&


# python sup_unsup_run.py --data_rep=nfstream --benign_sources Benign_only.csv Benign_only.csv --mal_sources labeled.csv --attack_types Malicious --num_agents=1 --model_name KDE --mal_folders CTU-IoT-Malware-Capture-34-1/  --benign_folders CTU-IoT-Malware-Capture-3-1/ CTU-IoT-Malware-Capture-1-1/ & 

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Benign_only.csv Benign_only.csv Benign_only.csv --mal_sources labeled.csv --attack_types Malicious --num_agents=1 --model_name KDE --mal_folders CTU-IoT-Malware-Capture-34-1/  --benign_folders CTU-IoT-Malware-Capture-3-1/ CTU-IoT-Malware-Capture-1-1/ CTU-IoT-Malware-Capture-20-1/& 




############################ IOT DATA #########################

# python sup_unsup_run.py --data_rep=nfstream --benign_sources CTU-IoT-Malware-Capture-21-1/Benign_only.csv --mal_sources CTU-IoT-Malware-Capture-3-1/labeled.csv --attack_types Malicious --num_agents=1 --model_name KDE --mal_folders IoT-CVS/  --benign_folders IoT-CVS/& 

# python sup_unsup_run.py --data_rep=nfstream --benign_sources CTU-IoT-Malware-Capture-20-1/Benign_only.csv --mal_sources CTU-IoT-Malware-Capture-3-1/labeled.csv  --attack_types Malicious --num_agents=1 --model_name KDE --mal_folders IoT-CVS/  --benign_folders IoT-CVS/& 

# python sup_unsup_run.py --data_rep=nfstream --benign_sources CTU-IoT-Malware-Capture-1-1/Benign_only.csv --mal_sources CTU-IoT-Malware-Capture-3-1/labeled.csv  --attack_types Malicious --num_agents=1 --model_name KDE --mal_folders IoT-CVS/  --benign_folders IoT-CVS/& 

# python sup_unsup_run.py --data_rep=nfstream --benign_sources CTU-IoT-Malware-Capture-34-1/Benign_only.csv --mal_sources CTU-IoT-Malware-Capture-3-1/labeled.csv --attack_types Malicious --num_agents=1 --model_name KDE --mal_folders IoT-CVS/  --benign_folders IoT-CVS/& 




# python sup_unsup_run.py --data_rep=nfstream --benign_sources  CTU-IoT-Malware-Capture-20-1/Benign_only.csv CTU-IoT-Malware-Capture-21-1/Benign_only.csv --mal_sources CTU-IoT-Malware-Capture-3-1/labeled.csv --attack_types Malicious --num_agents=1 --model_name KDE --mal_folders IoT-CVS/  --benign_folders IoT-CVS/& 


python sup_unsup_run.py --data_rep=nfstream --benign_sources CTU-IoT-Malware-Capture-34-1/Benign_only.csv CTU-IoT-Malware-Capture-1-1/Benign_only.csv  --mal_sources CTU-IoT-Malware-Capture-3-1/labeled.csv --attack_types Malicious --num_agents=1 --model_name KDE --mal_folders IoT-CVS/  --benign_folders IoT-CVS/& 

# python sup_unsup_run.py --data_rep=nfstream --benign_sources CTU-IoT-Malware-Capture-34-1/Benign_only.csv  CTU-IoT-Malware-Capture-20-1/Benign_only.csv  --mal_sources CTU-IoT-Malware-Capture-3-1/labeled.csv --attack_types Malicious --num_agents=1 --model_name KDE --mal_folders IoT-CVS/  --benign_folders IoT-CVS/& 

# python sup_unsup_run.py --data_rep=nfstream --benign_sources CTU-IoT-Malware-Capture-34-1/Benign_only.csv CTU-IoT-Malware-Capture-21-1/Benign_only.csv --mal_sources CTU-IoT-Malware-Capture-3-1/labeled.csv --attack_types Malicious --num_agents=1 --model_name KDE --mal_folders IoT-CVS/  --benign_folders IoT-CVS/& 

# python sup_unsup_run.py --data_rep=nfstream --benign_sources  CTU-IoT-Malware-Capture-1-1/Benign_only.csv CTU-IoT-Malware-Capture-20-1/Benign_only.csv  --mal_sources CTU-IoT-Malware-Capture-3-1/labeled.csv --attack_types Malicious --num_agents=1 --model_name KDE --mal_folders IoT-CVS/  --benign_folders IoT-CVS/& 

python sup_unsup_run.py --data_rep=nfstream --benign_sources  CTU-IoT-Malware-Capture-1-1/Benign_only.csv  CTU-IoT-Malware-Capture-21-1/Benign_only.csv --mal_sources CTU-IoT-Malware-Capture-3-1/labeled.csv --attack_types Malicious --num_agents=1 --model_name KDE --mal_folders IoT-CVS/  --benign_folders IoT-CVS/& 



# python sup_unsup_run.py --data_rep=nfstream --benign_sources CTU-IoT-Malware-Capture-1-1/Benign_only.csv CTU-IoT-Malware-Capture-20-1/Benign_only.csv CTU-IoT-Malware-Capture-21-1/Benign_only.csv --mal_sources CTU-IoT-Malware-Capture-34-1/labeled.csv  --attack_types Malicious --num_agents=1 --model_name KDE --mal_folders IoT-CVS/  --benign_folders IoT-CVS/& 

# python sup_unsup_run.py --data_rep=nfstream --benign_sources CTU-IoT-Malware-Capture-3-1/Benign_only.csv  CTU-IoT-Malware-Capture-20-1/Benign_only.csv CTU-IoT-Malware-Capture-1-1/Benign_only.csv --mal_sources CTU-IoT-Malware-Capture-34-1/labeled.csv --attack_types Malicious --num_agents=1 --model_name KDE --mal_folders IoT-CVS/  --benign_folders IoT-CVS/& 

# python sup_unsup_run.py --data_rep=nfstream --benign_sources CTU-IoT-Malware-Capture-3-1/Benign_only.csv CTU-IoT-Malware-Capture-1-1/Benign_only.csv  CTU-IoT-Malware-Capture-21-1/Benign_only.csv --mal_sources CTU-IoT-Malware-Capture-34-1/labeled.csv --attack_types Malicious --num_agents=1 --model_name KDE --mal_folders IoT-CVS/  --benign_folders IoT-CVS/& 

# python sup_unsup_run.py --data_rep=nfstream --benign_sources CTU-IoT-Malware-Capture-3-1/Benign_only.csv CTU-IoT-Malware-Capture-21-1/Benign_only.csv CTU-IoT-Malware-Capture-20-1/Benign_only.csv  --mal_sources CTU-IoT-Malware-Capture-34-1/labeled.csv --attack_types Malicious --num_agents=1 --model_name KDE --mal_folders IoT-CVS/  --benign_folders IoT-CVS/& 


# python sup_unsup_run.py --data_rep=nfstream --benign_sources CTU-IoT-Malware-Capture-3-1/Benign_only.csv CTU-IoT-Malware-Capture-1-1/Benign_only.csv CTU-IoT-Malware-Capture-20-1/Benign_only.csv CTU-IoT-Malware-Capture-21-1/Benign_only.csv --mal_sources CTU-IoT-Malware-Capture-34-1/labeled.csv --attack_types Malicious --num_agents=1 --model_name KDE --mal_folders IoT-CVS/  --benign_folders IoT-CVS/& 











##########################################

# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv Wednesday-14-02-2018/Benignonly.csv --mal_sources  Thursday-15-02-2018/DoS-Slowlorisonly.csv --attack_types DoS-Slowloris --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2017 CIC-IDS-2018&



# # ######################## Friday 16/02################
# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv Wednesday-14-02-2018/Benignonly.csv --mal_sources Friday-16-02-2018/DoS_Hulkonly.csv --attack_types DoS_Hulk --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2017 CIC-IDS-2018&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv Wednesday-14-02-2018/Benignonly.csv --mal_sources  Friday-16-02-2018/DDoS_SlowHTTPTestonly.csv --attack_types DDoS_SlowHTTPTest --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2017 CIC-IDS-2018&


################# We are training on the benign data of 2017 and testing the malicious data of 2018



######################## Wednesday 14/02################
# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv  --mal_sources Wednesday-14-02-2018/SSH-BruteForceonly.csv --attack_types SSH-BruteForce --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2017 &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv Wednesday-14-02-2018/Benignonly.csv --mal_sources  Wednesday-14-02-2018/FTP-BruteForceonly.csv --attack_types FTP-BruteForce --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2017 CIC-IDS-2018&


# # # ######################## Thursday 15/02################
# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv  --mal_sources Thursday-15-02-2018/DoS-GoldenEyeonly.csv --attack_types DoS-GoldenEye --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2017&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv  --mal_sources  Thursday-15-02-2018/DoS-Slowlorisonly.csv --attack_types DoS-Slowloris --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2017&



# # ######################## Friday 16/02################
# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv --mal_sources Friday-16-02-2018/DoS_Hulkonly.csv --attack_types DoS_Hulk --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2017&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv Wednesday-14-02-2018/Benignonly.csv --mal_sources  Friday-16-02-2018/DDoS_SlowHTTPTestonly.csv --attack_types DDoS_SlowHTTPTest --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2017 CIC-IDS-2018&




################# We are training on the benign data of 2018 and testing the malicious data of 2018



######################## Wednesday 14/02################
# python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv --mal_sources Wednesday-14-02-2018/SSH-BruteForceonly.csv --attack_types SSH-BruteForce --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2018 --benign_folders  CIC-IDS-2018&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv Wednesday-14-02-2018/Benignonly.csv --mal_sources  Wednesday-14-02-2018/FTP-BruteForceonly.csv --attack_types FTP-BruteForce --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2017 CIC-IDS-2018&


# # # ######################## Thursday 15/02################
# python sup_unsup_run.py --data_rep=nfstream --benign_sources  Wednesday-14-02-2018/Benignonly.csv --mal_sources Thursday-15-02-2018/DoS-GoldenEyeonly.csv --attack_types DoS-GoldenEye --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2018 --benign_folders  CIC-IDS-2018&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources  Wednesday-14-02-2018/Benignonly.csv --mal_sources  Thursday-15-02-2018/DoS-Slowlorisonly.csv --attack_types DoS-Slowloris --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2018 --benign_folders  CIC-IDS-2018&



# # ######################## Friday 16/02################
# python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv --mal_sources Friday-16-02-2018/DoS_Hulkonly.csv --attack_types DoS_Hulk --num_agents=1 --model_name GMM --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2018&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv Wednesday-14-02-2018/Benignonly.csv --mal_sources  Friday-16-02-2018/DDoS_SlowHTTPTestonly.csv --attack_types DDoS_SlowHTTPTest --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2017 CIC-IDS-2018&






















################ We are training on the benign data of 2017 and testing on the benign data of 2018



# python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv   --mal_sources  CIC-IDS-2017_Monday_Benign.csv --attack_types  empty --num_agents=1 --model_name GMM --mal_folders CIC-IDS-2017  --benign_folders CIC-IDS-2018&














# ################# We are training on the benign data of 2017 and 2018 and testing on the DDoS of 2017
# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv Wednesday-14-02-2018/Benignonly.csv --mal_sources CIC-IDS-2017_Friday_Bot.csv --attack_types Bot --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2017 CIC-IDS-2018&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv Wednesday-14-02-2018/Benignonly.csv --mal_sources CIC-IDS-2017_Friday_DDoS.csv  --attack_types DDoS  --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2017 CIC-IDS-2018&


# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv Wednesday-14-02-2018/Benignonly.csv --mal_sources  CIC-IDS-2017_Friday_Portscan.csv --attack_types Portscan  --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2017 CIC-IDS-2018&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv Wednesday-14-02-2018/Benignonly.csv --mal_sources  CIC-IDS-2017_Thursday_Infiltration.csv --attack_types Infiltration  --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2017 CIC-IDS-2018&


# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv Wednesday-14-02-2018/Benignonly.csv --mal_sources  CIC-IDS-2017_Thursday_WebAttack.csv --attack_types WebAttack  --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2017 CIC-IDS-2018&


# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv Wednesday-14-02-2018/Benignonly.csv --mal_sources  CIC-IDS-2017_Tuesday_FTP-Patator.csv --attack_types FTP-Patator  --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2017 CIC-IDS-2018&


# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv Wednesday-14-02-2018/Benignonly.csv --mal_sources  CIC-IDS-2017_Tuesday_SSH-Patator.csv --attack_types SSH-Patator  --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2017 CIC-IDS-2018&













# ################### We are training on  the benign data of 2018 and testing on the DDoS of 2018


###################### Wednesday 14/02################
#python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv --mal_sources Wednesday-14-02-2018/SSH-BruteForceonly.csv --attack_types SSH-BruteForce --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2018&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv --mal_sources  Wednesday-14-02-2018/FTP-BruteForceonly.csv --attack_types FTP-BruteForce --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2018&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Thursday-15-02-2018/Benignonly.csv --mal_sources Wednesday-14-02-2018/SSH-BruteForceonly.csv Wednesday-14-02-2018/FTP-BruteForceonly.csv --attack_types  SSH-BruteForce FTP-BruteForce --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2018&


# # ######################## Thursday 15/02################
#python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv --mal_sources Thursday-15-02-2018/DoS-GoldenEyeonly.csv --attack_types DoS-GoldenEye --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2018&

#python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv --mal_sources  Thursday-15-02-2018/DoS-Slowlorisonly.csv --attack_types DoS-Slowloris --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2018&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Friday-16-02-2018/Benignonly.csv --mal_sources Thursday-15-02-2018/DoS-GoldenEyeonly.csv Thursday-15-02-2018/DoS-Slowlorisonly.csv --attack_types DoS-GoldenEye DoS-Slowloris --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2018&


# ######################## Friday 16/02################
#python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv --mal_sources Friday-16-02-2018/DoS_Hulkonly.csv --attack_types DoS_Hulk --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2018&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv --mal_sources  Friday-16-02-2018/DDoS_SlowHTTPTestonly.csv --attack_types DDoS_SlowHTTPTest --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2018&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Friday-16-02-2018/Benignonly.csv --mal_sources Friday-16-02-2018/DoS_Hulkonly.csv  Friday-16-02-2018/DDoS_SlowHTTPTestonly.csv --attack_types  DoS_Hulk DDoS_SlowHTTPTest --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2018&









###################  We are training on the benign data of 2018 and testing on the DDoS of 2017


#python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv --mal_sources CIC-IDS-2017_Friday_Bot.csv --attack_types Bot --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2018&

#python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv --mal_sources CIC-IDS-2017_Friday_DDoS.csv  --attack_types DDoS  --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2018&


#python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv --mal_sources  CIC-IDS-2017_Friday_Portscan.csv --attack_types Portscan  --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2018&

#python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv --mal_sources  CIC-IDS-2017_Thursday_Infiltration.csv --attack_types Infiltration  --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2018&


#python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv --mal_sources  CIC-IDS-2017_Thursday_WebAttack.csv --attack_types WebAttack  --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2018&


#python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv --mal_sources  CIC-IDS-2017_Tuesday_FTP-Patator.csv --attack_types FTP-Patator  --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2018&


#python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv --mal_sources  CIC-IDS-2017_Tuesday_SSH-Patator.csv --attack_types SSH-Patator  --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2018&
















##### Benign 2017, Malicious 2017


# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv --mal_sources CIC-IDS-2017_Friday_Bot.csv --attack_types Bot --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2017&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv --mal_sources CIC-IDS-2017_Friday_DDoS.csv  --attack_types DDoS  --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2017&


# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv --mal_sources  CIC-IDS-2017_Friday_Portscan.csv --attack_types Portscan  --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2017&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv --mal_sources  CIC-IDS-2017_Thursday_Infiltration.csv --attack_types Infiltration  --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2017&


# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv --mal_sources  CIC-IDS-2017_Thursday_WebAttack.csv --attack_types WebAttack  --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2017&


# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv --mal_sources  CIC-IDS-2017_Tuesday_FTP-Patator.csv --attack_types FTP-Patator  --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2017&


# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv --mal_sources  CIC-IDS-2017_Tuesday_SSH-Patator.csv --attack_types SSH-Patator  --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2017&



# #### Benign 2017, Malicious 2018

# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv --mal_sources Wednesday-14-02-2018/SSH-BruteForceonly.csv --attack_types SSH-BruteForce --num_agents=1 --model_name GMM --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2017&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv --mal_sources  Wednesday-14-02-2018/FTP-BruteForceonly.csv --attack_types FTP-BruteForce --num_agents=1 --model_name GMM --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2017&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv --mal_sources Wednesday-14-02-2018/SSH-BruteForceonly.csv Wednesday-14-02-2018/FTP-BruteForceonly.csv --attack_types  SSH-BruteForce FTP-BruteForce --num_agents=1 --model_name GMM --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2017&


# # # ######################## Thursday 15/02################
# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv --mal_sources Thursday-15-02-2018/DoS-GoldenEyeonly.csv --attack_types DoS-GoldenEye --num_agents=1 --model_name GMM --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2017&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv --mal_sources  Thursday-15-02-2018/DoS-Slowlorisonly.csv --attack_types DoS-Slowloris --num_agents=1 --model_name GMM --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2017&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv --mal_sources Thursday-15-02-2018/DoS-GoldenEyeonly.csv Thursday-15-02-2018/DoS-Slowlorisonly.csv --attack_types DoS-GoldenEye DoS-Slowloris --num_agents=1 --model_name GMM --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2017&


# # ######################## Friday 16/02################
# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv --mal_sources Friday-16-02-2018/DoS_Hulkonly.csv --attack_types DoS_Hulk --num_agents=1 --model_name GMM --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2017&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv --mal_sources  Friday-16-02-2018/DDoS_SlowHTTPTestonly.csv --attack_types DDoS_SlowHTTPTest --num_agents=1 --model_name GMM --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2017&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv --mal_sources Friday-16-02-2018/DoS_Hulkonly.csv  Friday-16-02-2018/DDoS_SlowHTTPTestonly.csv --attack_types  DoS_Hulk DDoS_SlowHTTPTest --num_agents=1 --model_name GMM --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2017&






################# Benign 2018, Malicious 2017#####
# python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv --mal_sources CIC-IDS-2017_Friday_Bot.csv --attack_types Bot --num_agents=1 --model_name GMM --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2018&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv --mal_sources CIC-IDS-2017_Friday_DDoS.csv  --attack_types DDoS  --num_agents=1 --model_name GMM --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2018&


# python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv --mal_sources  CIC-IDS-2017_Friday_Portscan.csv --attack_types Portscan  --num_agents=1 --model_name GMM --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2018&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv --mal_sources  CIC-IDS-2017_Thursday_Infiltration.csv --attack_types Infiltration  --num_agents=1 --model_name GMM --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2018&


# python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv --mal_sources  CIC-IDS-2017_Thursday_WebAttack.csv --attack_types WebAttack  --num_agents=1 --model_name GMM --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2018&


# python sup_unsup_run.py --data_rep=nfstream --benign_sources Friday-16-02-2018/Benignonly.csv --mal_sources  CIC-IDS-2017_Tuesday_FTP-Patator.csv --attack_types FTP-Patator  --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2018&


# python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv --mal_sources  CIC-IDS-2017_Tuesday_SSH-Patator.csv --attack_types SSH-Patator  --num_agents=1 --model_name GMM --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2018&



# ############# Benign 2018, Malicious 2018#########

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Thursday-15-02-2018/Benignonly.csv --mal_sources Wednesday-14-02-2018/SSH-BruteForceonly.csv --attack_types SSH-BruteForce --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2018&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv --mal_sources  Wednesday-14-02-2018/FTP-BruteForceonly.csv --attack_types FTP-BruteForce --num_agents=1 --model_name GMM --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2018&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv --mal_sources Wednesday-14-02-2018/SSH-BruteForceonly.csv Wednesday-14-02-2018/FTP-BruteForceonly.csv --attack_types  SSH-BruteForce FTP-BruteForce --num_agents=1 --model_name GMM --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2018&


# # # ######################## Thursday 15/02################
# python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv --mal_sources Thursday-15-02-2018/DoS-GoldenEyeonly.csv --attack_types DoS-GoldenEye --num_agents=1 --model_name GMM --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2018&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Thursday-15-02-2018/Benignonly.csv --mal_sources  Thursday-15-02-2018/DoS-Slowlorisonly.csv --attack_types DoS-Slowloris --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2018&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv --mal_sources Thursday-15-02-2018/DoS-GoldenEyeonly.csv Thursday-15-02-2018/DoS-Slowlorisonly.csv --attack_types DoS-GoldenEye DoS-Slowloris --num_agents=1 --model_name GMM --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2018&


# ######################## Friday 16/02################
# python sup_unsup_run.py --data_rep=nfstream --benign_sources Thursday-15-02-2018/Benignonly.csv --mal_sources Friday-16-02-2018/DoS_Hulkonly.csv --attack_types DoS_Hulk --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2018&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv --mal_sources  Friday-16-02-2018/DDoS_SlowHTTPTestonly.csv --attack_types DDoS_SlowHTTPTest --num_agents=1 --model_name GMM --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2018&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv --mal_sources Friday-16-02-2018/DoS_Hulkonly.csv  Friday-16-02-2018/DDoS_SlowHTTPTestonly.csv --attack_types  DoS_Hulk DDoS_SlowHTTPTest --num_agents=1 --model_name GMM --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2018&



# ############# Benign 2017, Benign 2018#########

# python sup_unsup_run.py --data_rep=nfstream --benign_sources CIC-IDS-2017_Monday_Benign.csv --mal_sources Wednesday-14-02-2018/Benignonly.csv  --attack_types  --num_agents=1  -model_name GMM --mal_folders CIC-IDS-2018 --benign_folders CIC-IDS-2017&










##########################
#############################




# python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv --mal_sources CIC-IDS-2017_Friday_Bot.csv --attack_types Bot --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2018&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv --mal_sources CIC-IDS-2017_Friday_DDoS.csv  --attack_types DDoS  --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2018&


# python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv --mal_sources  CIC-IDS-2017_Friday_Portscan.csv --attack_types Portscan  --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2018&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv --mal_sources  CIC-IDS-2017_Thursday_Infiltration.csv --attack_types Infiltration  --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2018&


# python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv --mal_sources  CIC-IDS-2017_Thursday_WebAttack.csv --attack_types WebAttack  --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2018&


# python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv --mal_sources  CIC-IDS-2017_Tuesday_FTP-Patator.csv --attack_types FTP-Patator  --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2018&


# python sup_unsup_run.py --data_rep=nfstream --benign_sources Wednesday-14-02-2018/Benignonly.csv --mal_sources  CIC-IDS-2017_Tuesday_SSH-Patator.csv --attack_types SSH-Patator  --num_agents=1 --model_name KDE --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2018&













# # Increasing benign sources for GMM

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign Thursday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign Thursday_Benign Friday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 &

# # # # Changing model to OCSVM

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --model_name OCSVM --mal_folders CIC-IDS-2017 --benign_folders CIC-IDS-2017&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --model_name OCSVM &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --model_name OCSVM &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign Thursday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --model_name OCSVM &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign Thursday_Benign Friday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --model_name OCSVM &

# # # # Changing model to PCA

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --model_name PCA &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --model_name PCA &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --model_name PCA &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign Thursday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --model_name PCA &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign Thursday_Benign Friday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --model_name PCA &

# # # # Changing model to IF

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --model_name IF &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --model_name IF &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --model_name IF &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign Thursday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --model_name IF &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign Thursday_Benign Friday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --model_name IF &

# # # # Changing model to KDE

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --model_name KDE #&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --model_name KDE &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --model_name KDE &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign Thursday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --model_name KDE &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign Thursday_Benign Friday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --model_name KDE

# # Param search for GMM

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --n_components=2 &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --n_components=2

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --n_components=2 &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign Thursday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --n_components=2 &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign Thursday_Benign Friday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --n_components=2 &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --n_components=3 &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --n_components=3 &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --n_components=3 &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign Thursday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --n_components=3 &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign Thursday_Benign Friday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --n_components=3 &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --n_components=4 &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --n_components=4 &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --n_components=4 &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign Thursday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --n_components=4 &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign Thursday_Benign Friday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --n_components=4 &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --n_components=5 &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --n_components=5 &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --n_components=5 &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign Thursday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --n_components=5 &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign Thursday_Benign Friday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --n_components=5 


# Different attacks with KDE

# SSH-Patator

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign --mal_sources Tuesday_SSH-Patator --attack_types SSH-Patator --num_agents=1 --model_name KDE #&

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign --mal_sources Tuesday_SSH-Patator --attack_types SSH-Patator --num_agents=1 --model_name KDE &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign --mal_sources Tuesday_SSH-Patator --attack_types SSH-Patator --num_agents=1 --model_name KDE &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign Thursday_Benign --mal_sources Tuesday_SSH-Patator --attack_types SSH-Patator --num_agents=1 --model_name KDE &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign Thursday_Benign Friday_Benign --mal_sources Tuesday_SSH-Patator --attack_types SSH-Patator --num_agents=1 --model_name KDE &

# # FTP-Patator

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign --mal_sources Tuesday_FTP-Patator --attack_types FTP-Patator --num_agents=1 --model_name KDE &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign --mal_sources Tuesday_FTP-Patator --attack_types FTP-Patator --num_agents=1 --model_name KDE &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign --mal_sources Tuesday_FTP-Patator --attack_types FTP-Patator --num_agents=1 --model_name KDE &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign Thursday_Benign --mal_sources Tuesday_FTP-Patator --attack_types FTP-Patator --num_agents=1 --model_name KDE &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign Thursday_Benign Friday_Benign --mal_sources Tuesday_FTP-Patator --attack_types FTP-Patator --num_agents=1 --model_name KDE &

# # Wednesday DoS

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign --mal_sources Wednesday_DoS --attack_types DoS --num_agents=1 --model_name KDE &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign --mal_sources Wednesday_DoS --attack_types DoS --num_agents=1 --model_name KDE &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign --mal_sources Wednesday_DoS --attack_types DoS --num_agents=1 --model_name KDE &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign Thursday_Benign --mal_sources Wednesday_DoS --attack_types DoS --num_agents=1 --model_name KDE &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign Thursday_Benign Friday_Benign --mal_sources Wednesday_DoS --attack_types DoS --num_agents=1 --model_name KDE &

# # Thursday Infiltration

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign --mal_sources Thursday_Infiltration --attack_types Infiltration --num_agents=1 --model_name KDE &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign --mal_sources Thursday_Infiltration --attack_types Infiltration --num_agents=1 --model_name KDE &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign --mal_sources Thursday_Infiltration --attack_types Infiltration --num_agents=1 --model_name KDE &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign Thursday_Benign --mal_sources Thursday_Infiltration --attack_types Infiltration --num_agents=1 --model_name KDE &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign Thursday_Benign Friday_Benign --mal_sources Thursday_Infiltration --attack_types Infiltration --num_agents=1 --model_name KDE &

# # Thursday Webattack

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign --mal_sources Thursday_Infiltration --attack_types Infiltration --num_agents=1 --model_name KDE &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign --mal_sources Thursday_Infiltration --attack_types Infiltration --num_agents=1 --model_name KDE &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign --mal_sources Thursday_Infiltration --attack_types Infiltration --num_agents=1 --model_name KDE &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign Thursday_Benign --mal_sources Thursday_Infiltration --attack_types Infiltration --num_agents=1 --model_name KDE &

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign Thursday_Benign Friday_Benign --mal_sources Thursday_Infiltration --attack_types Infiltration --num_agents=1 --model_name KDE &
