import pathlib
import numpy as np

from sklearn.model_selection import train_test_split

from src.netml.utils.tool import dump_data, load_data, write_out, output_file_name

from src.netml.utils.data import read_data

from src.netml.utils.distribution import distribute_dataframe_np

import argparse
import configparser
import pandas as pd
import seaborn as sns

seed = 777

VERBOSITY = 6
import matplotlib.pyplot as plt
%matplotlib inline
rng = np.random.default_rng(seed)  # can be called without a seed

config = configparser.ConfigParser()
config.read_file(open('src/netml/configs/default_parks.cfg'))

parser = argparse.ArgumentParser()

combined = config.getboolean('DATA','combined')
distributed = config.getboolean('LEARNING','distributed')
alg_type = config['LEARNING']['alg_type']

# Input args
if 'CIC-IDS' in config['DATA']['data_source']:
    parser.add_argument('--data_rep',type=str,default='netml')
    parser.add_argument('--benign_sources',nargs='+')
    parser.add_argument('--mal_sources',nargs='+')
    parser.add_argument('--attack_types',nargs='+')
    if not combined:
        parser.add_argument('--train_sources',nargs='+',default=[])
        parser.add_argument('--test_sources',nargs='+',default=[])

parser.add_argument('--num_agents', type=int,default=1)
if distributed:
    # Federation args
    # imba for imbalanced split, seq_select to split data in order of appearance
    parser.add_argument('--imba', dest='imba', action='store_true')
    parser.add_argument('--seq_select', dest='seq_select', action='store_true')
if 'CIC-IDS' in config['DATA']['data_source']:
    data_source=config['DATA']['data_source']
elif 'BAS' in config['DATA']['data_source']:
    data_source='BAS'
if not combined:
    assert len(args.benign_sources)+len(args.mal_sources)==len(args.train_sources)+len(args.test_sources)
# parse arguments
args = parser.parse_args("--data_rep=nfstream --benign_sources Monday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1".split())
# Load data
print('Loading data')
X_train, y_train, X_test, y_test, column_names = read_data(args, config, data_source, args.data_rep, float(config['DATA']['train_test_split']),rng,alg_type,combined)

print(column_names)

if args.num_agents>1:
    df_list=distribute_dataframe_np(X_train, y_train, args.num_agents, args.imba, args.seq_select, rng, label_name=column_names[-1])
else:
    df_list=[(X_train,y_train)]
train_df = pd.DataFrame(data = X_train.astype(float), 
                  columns = column_names[:9])
train_df['Label']=y_train
test_df = pd.DataFrame(data = X_test.astype(float), 
                  columns = column_names[:9])
test_df['Label']=y_test
test_df_benign=test_df[test_df['Label']==0.0]
test_df_mal=test_df[test_df['Label']==1.0]
fig, axs = plt.subplots(ncols=3,nrows=3,figsize=(11,9),gridspec_kw={'hspace': 0.3})
for i,name in enumerate(column_names[:9]):
    row_index=int(i/3)
    col_index=int(i%3)
    sns.kdeplot(data=train_df, x=name,ax=axs[row_index][col_index])
fig, axs = plt.subplots(ncols=3,nrows=3,figsize=(11,9),gridspec_kw={'hspace': 0.3})
for i,name in enumerate(column_names[:9]):
    row_index=int(i/3)
    col_index=int(i%3)
    sns.kdeplot(data=test_df_benign, x=name,ax=axs[row_index][col_index])
# parse arguments
args = parser.parse_args("--data_rep=nfstream --benign_sources Tuesday_Benign --mal_sources Friday_DDoS --attack_types DDoS --num_agents=1".split())
# Load data
print('Loading data')
X_train, y_train, X_test, y_test, column_names = read_data(args, config, data_source, args.data_rep, float(config['DATA']['train_test_split']),rng,alg_type,combined)

print(column_names)

if args.num_agents>1:
    df_list=distribute_dataframe_np(X_train, y_train, args.num_agents, args.imba, args.seq_select, rng, label_name=column_names[-1])
else:
    df_list=[(X_train,y_train)]
train_df = pd.DataFrame(data = X_train.astype(float), 
                  columns = column_names[:9])
train_df['Label']=y_train
test_df = pd.DataFrame(data = X_test.astype(float), 
                  columns = column_names[:9])
test_df['Label']=y_test
test_df_benign=test_df[test_df['Label']==0.0]
test_df_mal=test_df[test_df['Label']==1.0]
fig, axs = plt.subplots(ncols=3,nrows=3,figsize=(11,9),gridspec_kw={'hspace': 0.3})
for i,name in enumerate(column_names[:9]):
    row_index=int(i/3)
    col_index=int(i%3)
    sns.kdeplot(data=train_df, x=name,ax=axs[row_index][col_index])
fig, axs = plt.subplots(ncols=3,nrows=3,figsize=(11,9),gridspec_kw={'hspace': 0.3})
for i,name in enumerate(column_names[:9]):
    row_index=int(i/3)
    col_index=int(i%3)
    sns.kdeplot(data=test_df_benign, x=name,ax=axs[row_index][col_index])
fig, axs = plt.subplots(ncols=3,nrows=3,figsize=(11,9),gridspec_kw={'hspace': 0.3})
for i,name in enumerate(column_names[:9]):
    row_index=int(i/3)
    col_index=int(i%3)
    sns.kdeplot(data=test_df_mal, x=name,ax=axs[row_index][col_index])
