"""Common functions.

"""
# Authors: kun.bj@outlook.com
#
# License: xxx

import os
import pickle
import time
from functools import wraps
from datetime import datetime

import pandas as pd
import json
from joblib import dump, load


class ManualDependencyError(RuntimeError):
    pass

def output_file_name(config,args):
#     output_dir_name=config['DATA']['output_dir']+'/'+config['DATA']['data_source']+'/'+config['LEARNING']['alg_type']+'/'+args.data_rep

#     if not os.path.exists(output_dir_name):
#         os.makedirs(output_dir_name)

#     out_file_name=output_dir_name+'/'+args.model_name
#     if args.imba:
#         out_file_name+='_imba'
#     if args.seq_select:
#         out_file_name+='_seq'
    output_dir_name=config['DATA']['output_dir']+'/'+"IoT"
    if not os.path.exists(output_dir_name):
        os.makedirs(output_dir_name) 
    output_dir_name= output_dir_name+"/unsupervised"
    if not os.path.exists(output_dir_name):
        os.makedirs(output_dir_name)
    out_file_name = output_dir_name + "/"+args.model_name
    
    
    return out_file_name

def write_out(file_name, config, args, params,train_time, test_time, test_perf, ben_accs=None, mal_accs=None):
    
    out_file_name=output_file_name(config,args)
    print(out_file_name)
    out_file_name+='.txt'

    if config['LEARNING']['alg_type']=='unsupervised':
        output_dict = {"benign_sources": args.benign_sources,
            "mal_sources": args.mal_sources,
            "combined": config['DATA']['combined'],
            "attacks": args.attack_types, 
            "params": params,
            "num_splits": args.num_agents,
            "auc": test_perf,
            "train_time": train_time,
            "test_time": test_time,
            "sample_level":args.sample_level
            }
    elif config['LEARNING']['alg_type']=='supervised':
        output_dict = {"benign_sources": args.benign_sources,
            "mal_sources": args.mal_sources,
            "combined": config['DATA']['combined'],
            "attacks": args.attack_types, 
            "params": params,
            "num_splits": args.num_agents,
            "overall_classification": test_perf,
            "benign_classification": ben_accs,
            "mal_classification": mal_accs,
            "train_time": train_time,
            "test_time": test_time,
            "sample_level": args.sample_level
            }
    if config.getboolean('DATA','combined'):
        output_dict["train-test-split"] = float(config['DATA']['train_test_split'])
    else:
        output_dict["train days"] = args.train_sources
        output_dict["test_days"] = args.test_sources

    if config.getboolean('LEARNING','distributed'):
        if args.imba:
            output_dict['imbalanced']= 'True'
        if args.seq_select:
            output_dict['seq_select']= 'True'
    
    with open(out_file_name, 'a') as json_file:
        json.dump(output_dict, json_file)
        json_file.write('\n')


def dump_data(data, out_file, verbose=True):
    """Save data to pickle file

    Parameters
    ----------
    data: any data

    out_file: str (path) or file
        out file

    verbose: bool (default True)
        a print level is to control what information should be printed according to the given value.
        The higher the value is, the more info is printed.

    Returns
    -------

    """
    # won't close descriptor we don't open
    try:
        out_desc = None  # avoid UnboundLocalError in finally

        if hasattr(out_file, 'write'):
            out_desc = out_file
        elif out_file:
            # FIXME: overwrite=verbose?
            check_path(out_file, overwrite=verbose)
            out_desc = open(out_file, 'wb')
        else:
            raise TypeError("out_file argument required")

        dump(data, out_desc)
    finally:
        if out_desc is not None and out_desc is not out_file:
            # it's ours to manage
            out_desc.close()


def load_data(in_file):
    """load data from pickle file

    Parameters
    ----------
    in_file: str (path) or file
        input file

    Returns
    -------
    loaded data structure

    """
    try:
        in_desc = None  # avoid UnboundLocalError in finally

        if hasattr(in_file, 'read'):
            in_desc = in_file
        else:
            in_desc = open(in_file, 'rb')

        return pickle.load(in_desc)
    finally:
        if in_desc is not None and in_desc is not in_file:
            in_desc.close()


def data_info(data=None, name='data'):
    """Print data basic information

    Parameters
    ----------
    data: array

    name: str
        data name

    Returns
    -------

    """

    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 100)
    pd.set_option('display.float_format', lambda x: '%.3f' % x)  # without scientific notation

    columns = ['col_' + str(i) for i in range(data.shape[1])]
    dataset = pd.DataFrame(data=data, index=range(data.shape[0]), columns=columns)
    print(f'{name}.shape: {data.shape}')
    print(dataset.describe())
    print(dataset.info(verbose=True))


def check_path(file_path, overwrite=True):
    """Check if a path is existed or not.
     If the path doesn't exist, then create it.

    Parameters
    ----------
    file_path: str

    overwrite: boolean (default is True)
        if the path exists, delete all data in it and create a new one

    Returns
    -------

    """
    path_dir = os.path.dirname(file_path)
    if not os.path.exists(path_dir) and len(path_dir) > 0:
        os.makedirs(path_dir)

    if os.path.exists(file_path):
        if overwrite:
            os.remove(file_path)

    return file_path


def timing(func):
    """Calculate the execute time of the given func"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        st = datetime.fromtimestamp(start).strftime('%Y-%m-%d %H:%M:%S')
        print(f'\'{func.__name__}()\' starts at {st}')
        result = func(*args, **kwargs)
        end = time.time()
        ed = datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S')
        tot_time = (end - start) / 60
        tot_time = float(f'{tot_time:.4f}')
        print(f'\'{func.__name__}()\' ends at {ed} and takes {tot_time} mins.')
        func.tot_time = tot_time  # add new variable to func
        return result, tot_time

    return wrapper
