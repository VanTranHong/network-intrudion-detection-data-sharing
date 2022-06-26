#!/bin/bash

# Changing model to SVM

# python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --model_name SVM

python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --model_name RF # &

#python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --model_name SVM &

#python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign Thursday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --model_name SVM &

#python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign Thursday_Benign Friday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --model_name SVM &

# Changing model to RF

#python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --model_name RF &

#python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --model_name RF &

#python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --model_name RF &

#python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign Thursday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --model_name RF &

#python sup_unsup_run.py --data_rep=nfstream --benign_sources Monday_Benign Tuesday_Benign Wednesday_Benign Thursday_Benign Friday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1 --model_name RF
