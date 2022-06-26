import pandas as pd, numpy as np, glob
import sys, os
from nfstream import NFStreamer, NFPlugin
import argparse

# fname = sys.argv[1]

parser = argparse.ArgumentParser(description="")

parser.add_argument("--day",type=str)
parser.add_argument("--year",type=int)

args = parser.parse_args()

if args.year==2018:
    base_path='/Users/arjunbhagoji/IDS_data/IDS_2018/'
    day_name=args.day
    input_files = glob.glob(base_path+'pcaps/'+day_name+'/pcap/*.pcap')
    out_dir=base_path+'flows/nfstream/'+day_name+'/'
elif args.year==2017:
    base_path='/Users/arjunbhagoji/IDS_data/IDS_2017/'
    day_name=args.day
    input_files = glob.glob(base_path+'PCAPs/'+day_name+'*.pcap')
    print(base_path+'PCAPs/'+day_name+'*.pcap')
    out_dir=base_path+'flows/nfstream/'+day_name+'/'
elif args.year==9999:
    base_path='/home/abhagoji/netml-dpkt/examples/data/'
    input_files = glob.glob(base_path+'*.pcap')
    out_dir=base_path+'flows/'
list_of_dfs=[]
if not os.path.isdir(out_dir):
    os.mkdir(out_dir)
for i,fname in enumerate(input_files):
    active_timeout, idle_timeout = (60, 30)
    df = NFStreamer(source=fname, active_timeout=active_timeout, idle_timeout=idle_timeout).to_pandas()
    list_of_dfs.append(df)
    if i%10==0:
#         print(day_name,i,fname)
        print(i,fname)
        df_out = pd.concat(list_of_dfs, axis=0, ignore_index=True)
        out_path=out_dir+str(int(i/10))
        df_out.to_csv(out_path+'.csv')
        list_of_dfs=[]
