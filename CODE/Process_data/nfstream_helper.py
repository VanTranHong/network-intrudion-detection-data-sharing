import pandas as pd, numpy as np, glob
import sys, os
from nfstream import NFStreamer, NFPlugin

folder = "/data/vantran/Arjun/nds/IoT-data/IoT-23-Dataset/"
sub_folder = "CTU-IoT-Malware-Capture-21-1/"
fname = "2018-10-03-15-22-32-192.168.100.113.pcap"

csv_folder = "/data/vantran/Arjun/nds/IoT-data/IoT-CVS/"

path = csv_folder + sub_folder
if  not os.path.exists(path):
    os.makedirs(path)



csv_fname = fname.replace(".pcap",".csv")
active_timeout, idle_timeout = (120, 30)
df = NFStreamer(source=folder+sub_folder+fname, active_timeout=active_timeout, idle_timeout=idle_timeout).to_pandas()
df.to_csv(path + csv_fname)

