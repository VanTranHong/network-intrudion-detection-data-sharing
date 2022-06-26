import pandas as pd
import numpy as np
import os



filename = "/data/vantran/Arjun/nds/IoT-data/IoT-23-Dataset/"
folder_ = "CTU-IoT-Malware-Capture-34-1/"
f_ = "bro/conn.log.labeled"
file_ = open(filename+folder_+f_, 'r')
lines = file_.read().splitlines()

fields = lines[6]
types = lines[7]
columns_name = fields.split()[1:]
print(columns_name)
dat = []

for i in range(8, len(lines)):
    line = lines[i].split()
    dat.append(line)
print(dat[:5])

df = pd.DataFrame(dat, columns = columns_name)


folder = "/data/vantran/Arjun/nds/IoT-data/IoT-CVS/" 
if os.path.isdir(folder + folder_) == False:
    os.mkdir(folder + folder_)
    print(folder + folder_)
fname = "label.csv"
new_name = folder+folder_+fname
print(df)
df.to_csv(new_name, encoding='utf-8')
