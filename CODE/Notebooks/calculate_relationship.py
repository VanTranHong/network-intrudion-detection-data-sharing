import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import random
from sklearn.metrics.cluster import adjusted_mutual_info_score
from scipy.stats import wasserstein_distance

file1_1 = "/data/vantran/Arjun/nds/IoT-data/IoT-CVS/CTU-IoT-Malware-Capture-1-1/Benign_only.csv"
file3_1 = "/data/vantran/Arjun/nds/IoT-data/IoT-CVS/CTU-IoT-Malware-Capture-3-1/Benign_only.csv"
file20_1 = "/data/vantran/Arjun/nds/IoT-data/IoT-CVS/CTU-IoT-Malware-Capture-20-1/Benign_only.csv"
file21_1 = "/data/vantran/Arjun/nds/IoT-data/IoT-CVS/CTU-IoT-Malware-Capture-21-1/Benign_only.csv"
file34_1 = "/data/vantran/Arjun/nds/IoT-data/IoT-CVS/CTU-IoT-Malware-Capture-34-1/Benign_only.csv"

df1 = pd.read_csv(file1_1)
df3 = pd.read_csv(file3_1)
df20=pd.read_csv(file20_1)
df21=pd.read_csv(file21_1)
df34=pd.read_csv(file34_1) 
df_list = [df1,df3,df20,df21,df34]

dict_df = {"df1":df1,"df3":df3,"df20":df20,"df21":df21,"df34":df34}

columns_to_check = ['bidirectional_first_seen_ms', 'bidirectional_last_seen_ms',
                    'bidirectional_duration_ms', 'bidirectional_packets',
       'bidirectional_bytes','src2dst_first_seen_ms', 'src2dst_last_seen_ms',
                    'src2dst_duration_ms', 'src2dst_packets',
       'src2dst_bytes', 'dst2src_duration_ms','dst2src_first_seen_ms', 'dst2src_last_seen_ms',
                    'dst2src_packets',
       'dst2src_bytes']

def combine_df(df_list):
    dimensions = [df.shape[0] for df in df_list]
    min_dim = min(dimensions)
    li_shuffled = []
    for df in df_list:
        df_shuffled = list(range(df.shape[0]))
        random.seed(0)
        random.shuffle(df_shuffled)
        df_shuffled=df[:min_dim]
        li_shuffled.append(df_shuffled)
    return pd.concat(li_shuffled, axis=0, ignore_index=True)
df1_3 = combine_df([df1,df3])
df1_20 = combine_df([df1,df20])
df1_21 = combine_df([df1,df21])
df1_34 = combine_df([df1,df34])
df3_20 = combine_df([df3,df20])
df3_21 = combine_df([df3,df21])
df3_34 = combine_df([df3,df34])
df20_21 = combine_df([df21,df20])
df20_34 = combine_df([df34,df20])
df21_34 = combine_df([df21,df34])




df_1_3_20 = combine_df([df1,df3,df20])
df_1_3_21 = combine_df([df1,df3,df21])
df_1_3_34 = combine_df([df1,df3,df34])
df_1_20_21 = combine_df([df1,df20,df21])
df_1_20_34 = combine_df([df1,df20,df34])
df_1_21_34 = combine_df([df1,df21,df34])
df_3_20_21 = combine_df([df3,df20,df21])
df_3_20_34 = combine_df([df3,df20,df34])
df_3_21_34 = combine_df([df3,df21,df34])
df_20_21_34 = combine_df([df20,df21,df34])

df_1_3_20_21 = combine_df([df1,df3,df20,df21])
df_1_3_20_34 = combine_df([df1,df3,df20,df34])
df_1_3_21_34 = combine_df([df1,df3,df21,df34])
df_1_20_21_34 = combine_df([df1,df20,df21,df34])
df_3_20_21_34 = combine_df([df3,df20,df21,df34])

def process_df(df1, df2):
    sample_size = min(df1.shape[0],df2.shape[0])
    df1 = df1[columns_to_check]
    df1_shuffled = list(range(df1.shape[0]))
    random.shuffle(df1_shuffled)
    df1_shuffled=df1_shuffled[:sample_size]
    df2 = df2[columns_to_check]
    df2_shuffled = list(range(df2.shape[0]))
    random.shuffle(df2_shuffled)
    df2_shuffled=df2_shuffled[:sample_size]
    df1_filtered = df1.iloc[df1_shuffled]
    df2_filtered = df2.iloc[df2_shuffled]
    
    
    for col in df1_filtered.columns:
        col1 = df1_filtered[col]
        col2 = df2_filtered[col]
        max_val = max(max(list(col1)), max(list(col2)))
        col1_new = [val/max_val for val in col1]
        col2_new = [val/max_val for val in col2]
        df1_filtered[col] = col1_new
        df2_filtered[col] = col2_new
    
        
        
        
    
    
    return df1_filtered,df2_filtered

    

def calculate_mutualinfo(df1_, df2_):
    df1,df2 = process_df(df1_,df2_)
    total_score = []
    for col in columns_to_check:
        total_score.append(adjusted_mutual_info_score(df1[col], df2[col]))
    return total_score
def cal_wasserstein_dist(df1_, df2_):
    df1,df2 = process_df(df1_,df2_)
    total_score = []
    for col in columns_to_check:
        total_score.append(wasserstein_distance(df1[col], df2[col]))
    return total_score
  
##### calculating the relationship bewteen dataframes
info_list = []
distance_list = []






for i in range(len(df_list)):
    mutual_info=[]
    w_distance = []
    
    df1 = df_list[i]
    for j in range(len(df_list)):
        
        if j!= i:
            df2 = df_list[j]
            info = sum([abs(val) for val in calculate_mutualinfo(df1, df2)])
            distance = sum(cal_wasserstein_dist(df1, df2))
            mutual_info.append(info)
            w_distance.append(distance)
        else:
            mutual_info.append(0)
            w_distance.append(0)
    info_list.append(mutual_info)
    distance_list.append(w_distance)
df_info = pd.DataFrame(info_list, columns = ["Df1", "Df3", "Df20","Df21", "Df34"])
df_distance = pd.DataFrame(distance_list, columns = ["Df1", "Df3", "Df20","Df21", "Df34"])
df_info.to_csv("/data/vantran/Arjun/nds/IoT-data/IoT-CVS/mutual_info_between_df.csv")
df_distance.to_csv("/data/vantran/Arjun/nds/IoT-data/IoT-CVS/wasserstein_dist_between_df.csv")


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

filename = "/data/vantran/Arjun/nds/IoT-data/IoT-CVS/mutual_info_between_df.csv"
df_mutual_info = pd.read_csv(filename)
df_mutual_info = df_mutual_info.drop(["Unnamed: 0"],axis =1)
print(df_mutual_info)
names = ["Df1","Df3","Df20","Df21","Df34"]
df_mutual_info.index = names
ax = plt.axes()



sns.heatmap(df_mutual_info,ax=ax,cmap = "Blues", annot=True,xticklabels=names, yticklabels=names)
ax.set_title('Mutual information between dataset')
The_keys_34 = ['1', '3', '20', '21', '20&21', '1&3', '1&20', '20&3', '1&21', '21&3', '1&20&21', '1&21&3', '20&21&3', '1&20&3', '1&20&21&3']
The_keys_3 = ['1','21','20','34','1&21','1&20','20&21','1&34','21&34','20&34','1&20&21','1&21&34','20&21&34','1&20&34','1&20&21&34']
##### finding and plotting the relationship on the test set 3-1
mutual=[]
distance = []


for train in The_keys_3:
    df_train = train.split("&")
    train_list = []
    for df in df_train:
        name_df = "df"+df
        train_list.append(dict_df[name_df])
    combined_train = combine_df(train_list)
    info = sum([abs(val) for val in calculate_mutualinfo(combined_train, dict_df["df3"])])
    dis = sum(cal_wasserstein_dist(combined_train, dict_df["df3"]))
    mutual.append(info)
    distance.append(dis)
print(mutual)
print(distance)
colors = ['g','blue','orange','red','purple', 'grey','yellow','brown','black', 'pink']
X = [i for i in range(len(The_keys_3))]
plt.bar(X , distance, color = colors[0], width = 0.25)
# plt.bar([x+0.25 for x in X] , distance, color = colors[1], width = 0.25)

plt.legend(["distance"])
plt.xticks(X, The_keys_3, fontsize=15, rotation=90)
plt.yticks(fontsize=15)
plt.xlabel('Train set',fontsize = 20)
plt.ylabel('Distance score', fontsize=20)
plt.title("Distancec score with 3-1 testset", fontsize=15)
plt.show() 
##### finding and plotting the relationship on the test set 34-1
mutual_=[]
distance_ = []


for train in The_keys_34:
    df_train = train.split("&")
    train_list = []
    for df in df_train:
        name_df = "df"+df
        train_list.append(dict_df[name_df])
    combined_train = combine_df(train_list)
    info = sum([abs(val) for val in calculate_mutualinfo(combined_train, dict_df["df34"])])
    distance = sum(cal_wasserstein_dist(combined_train, dict_df["df34"]))
    mutual_.append(info)
    distance_.append(distance)
print(mutual_)
print(distance_)
colors = ['g','blue','orange','red','purple', 'grey','yellow','brown','black', 'pink']
X = [i for i in range(len(The_keys_34))]
plt.bar(X , mutual_, color = colors[0], width = 0.25)
# plt.bar([x+0.25 for x in X] , distance, color = colors[1], width = 0.25)

plt.legend(["Mutual info"])
plt.xticks(X, The_keys_34, fontsize=15, rotation=90)
plt.yticks(fontsize=15)
plt.xlabel('Train set',fontsize = 20)
plt.ylabel('Mutual information score', fontsize=20)
plt.title("Mutual information score with 34-1 testset", fontsize=15)
plt.show() 

                       

                       
