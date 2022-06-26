#!/bin/bash

python sup_unsup_run.py --data_rep=nfstream --benign_sources BAS_2021-04-09_12-41-44_86400_ml  --mal_sources CIC-IDS-2017_Friday_Portscan --attack_types=Portscan  --num_agents=1 --model_name=GMM &

python sup_unsup_run.py --data_rep=nfstream --benign_sources BAS_2021-04-09_12-41-44_86400_ml  --mal_sources CIC-IDS-2017_Friday_Portscan --attack_types=Portscan  --num_agents=1 --model_name=OCSVM &

python sup_unsup_run.py --data_rep=nfstream --benign_sources BAS_2021-04-09_12-41-44_86400_ml  --mal_sources CIC-IDS-2017_Friday_Portscan --attack_types=Portscan  --num_agents=1 --model_name=PCA &

python sup_unsup_run.py --data_rep=nfstream --benign_sources BAS_2021-04-09_12-41-44_86400_ml  --mal_sources CIC-IDS-2017_Friday_Portscan --attack_types=Portscan  --num_agents=1 --model_name=KDE &

python sup_unsup_run.py --data_rep=nfstream --benign_sources BAS_2021-04-09_12-41-44_86400_ml  --mal_sources CIC-IDS-2017_Friday_Portscan --attack_types=Portscan  --num_agents=1 --model_name=IF &

# Attack to DDoS

python sup_unsup_run.py --data_rep=nfstream --benign_sources BAS_2021-04-09_12-41-44_86400_ml  --mal_sources CIC-IDS-2017_Friday_DDoS --attack_types=DDoS  --num_agents=1 --model_name=GMM &

python sup_unsup_run.py --data_rep=nfstream --benign_sources BAS_2021-04-09_12-41-44_86400_ml  --mal_sources CIC-IDS-2017_Friday_DDoS --attack_types=DDoS  --num_agents=1 --model_name=OCSVM &

python sup_unsup_run.py --data_rep=nfstream --benign_sources BAS_2021-04-09_12-41-44_86400_ml  --mal_sources CIC-IDS-2017_Friday_DDoS --attack_types=DDoS  --num_agents=1 --model_name=PCA &

python sup_unsup_run.py --data_rep=nfstream --benign_sources BAS_2021-04-09_12-41-44_86400_ml  --mal_sources CIC-IDS-2017_Friday_DDoS --attack_types=DDoS  --num_agents=1 --model_name=KDE &

python sup_unsup_run.py --data_rep=nfstream --benign_sources BAS_2021-04-09_12-41-44_86400_ml  --mal_sources CIC-IDS-2017_Friday_DDoS --attack_types=DDoS  --num_agents=1 --model_name=IF &
