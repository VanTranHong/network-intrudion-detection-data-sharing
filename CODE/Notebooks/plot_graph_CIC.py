import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import statistics as stat
def read_file(file_name):
    f = open(file_name, "r")
    string = f.read()
    return string
#### Plot histogram
def plot_histogram(values, name):
    values = [np.log(value+0.00001) for value in values]
    values = [max(0,value) for value in values]
    
    n, bins, patches = plt.hist(x=values, bins=np.linspace(0,11,100), color='#0504aa',
                                alpha=0.7, rwidth=0.85)

    
    print(min(values))
    print(max(values))
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram of log distribution of '+ name )
    maxfreq = n.max()
    print("The mean value is")
    print(stat.mean(values))
    print("standard deviation is")
    print(stat.stdev(values))
    # Set a clean upper y-axis limit.
    plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
    
cols = ['protocol',
       'bidirectional_first_seen_ms', 'bidirectional_last_seen_ms',
       'bidirectional_duration_ms', 'bidirectional_packets',
       'bidirectional_bytes', 'src2dst_first_seen_ms', 'src2dst_last_seen_ms',
       'src2dst_duration_ms', 'src2dst_packets', 'src2dst_bytes',
       'dst2src_first_seen_ms', 'dst2src_last_seen_ms', 'dst2src_duration_ms',
       'dst2src_packets', 'dst2src_bytes', 'ts',
       'duration']
col_name = cols[17]
########### No sampling for 2017


file_name = "/data/vantran/Arjun/nds/IoT-data/IoT-CVS/CTU-IoT-Malware-Capture-1-1/Malicious_only.csv"
df = pd.read_csv(file_name)
# print(df[col_name].unique())
# p_17 = df[df[col_name]==17]
# print(p_17.shape)

# p_6 = df[df[col_name]==6]
# print(p_6.shape)
# print(p_17.shape[0]/(p_17.shape[0] + p_6.shape[0]))
# print(p_6.shape[0]/(p_17.shape[0] + p_6.shape[0]))
# # df = df.drop(columns = ["Unnamed: 0","Unnamed: 0.1"], axis = 0)

# val = df[col_name]
# min_ = min(val)
# max_ = max(val)


plot_histogram(list(df[col_name]), col_name)

########### No sampling for 2017


file_name = "/data/vantran/Arjun/nds/IoT-data/IoT-CVS/CTU-IoT-Malware-Capture-3-1/Malicious_only.csv"
df = pd.read_csv(file_name)
# print(df[col_name].unique())
# p_17 = df[df[col_name]==17]
# print(p_17.shape)

# p_6 = df[df[col_name]==6]
# print(p_6.shape)
# print(p_17.shape[0]/(p_17.shape[0] + p_6.shape[0]))
# print(p_6.shape[0]/(p_17.shape[0] + p_6.shape[0]))
# # df = df.drop(columns = ["Unnamed: 0","Unnamed: 0.1"], axis = 0)

# val = df[col_name]
# min_ = min(val)
# max_ = max(val)


plot_histogram(list(df[col_name]), col_name)
########### No sampling for 2017


file_name = "/data/vantran/Arjun/nds/IoT-data/IoT-CVS/CTU-IoT-Malware-Capture-20-1/Malicious_only.csv"
df = pd.read_csv(file_name)
# print(df[col_name].unique())
# p_17 = df[df[col_name]==17]
# print(p_17.shape)

# p_6 = df[df[col_name]==6]
# print(p_6.shape)
# print(p_17.shape[0]/(p_17.shape[0] + p_6.shape[0]))
# print(p_6.shape[0]/(p_17.shape[0] + p_6.shape[0]))
# # df = df.drop(columns = ["Unnamed: 0","Unnamed: 0.1"], axis = 0)

# val = df[col_name]
# min_ = min(val)
# max_ = max(val)


plot_histogram(list(df[col_name]), col_name)
########### No sampling for 2017


file_name = "/data/vantran/Arjun/nds/IoT-data/IoT-CVS/CTU-IoT-Malware-Capture-21-1/Malicious_only.csv"
df = pd.read_csv(file_name)
# print(df[col_name].unique())
# p_17 = df[df[col_name]==17]
# print(p_17.shape)

# p_6 = df[df[col_name]==6]
# print(p_6.shape)
# print(p_17.shape[0]/(p_17.shape[0] + p_6.shape[0]))
# print(p_6.shape[0]/(p_17.shape[0] + p_6.shape[0]))
# # df = df.drop(columns = ["Unnamed: 0","Unnamed: 0.1"], axis = 0)

# val = df[col_name]
# min_ = min(val)
# max_ = max(val)


plot_histogram(list(df[col_name]), col_name)

def non_sampling_scores(string):

    strings = string.split("\n")
    big_dict = {}
    for string in strings:
        if string != "":
            dic = eval(string)
            train = "-".join(dic["benign_sources"])
            test = "-".join(dic["mal_sources"])
            score = dic["auc"][0]
            if train not in big_dict.keys():
                big_dict[train]={}

            sub_dic = big_dict[train]
            sub_dic[test]=score
    keys = list(big_dict.keys())
    return keys, big_dict

# Declaring the figure or the plot (y, x) or (width, height)
attack_list = ['CIC-IDS-2017_Tuesday_FTP-Patator.csv', 'CIC-IDS-2017_Thursday_Infiltration.csv', 'CIC-IDS-2017_Friday_Bot.csv', 'CIC-IDS-2017_Friday_DDoS.csv', 'CIC-IDS-2017_Thursday_WebAttack.csv', 'CIC-IDS-2017_Tuesday_SSH-Patator.csv', 'CIC-IDS-2017_Friday_Portscan.csv', 'Friday-16-02-2018/DoS_Hulkonly.csv', 'Thursday-15-02-2018/DoS-Slowlorisonly.csv', 'Thursday-15-02-2018/DoS-GoldenEyeonly.csv', 'Wednesday-14-02-2018/SSH-BruteForceonly.csv']
attack_color = ['black','black','black','black','black','black','black','blue','blue','blue','blue']
attacks = ['FTP-Patator\n2017', 'Infiltration\n2017','Bot\n2017','DDoS\n2017','WebAttack\n2017','SSH-Patator\n2017',
          'Portscan\n2017','DoS_Hulk\n2018','DoS-Slowloris\n2018','DoS-GoldenEye\n2018','SSH-BruteForce\n2018']
X = np.arange(len(attack_list))

def plot_graph(keys, results):
    colors = ['g','blue','orange','red','purple', 'grey','yellow','brown','black', 'pink']
    plt.figure(figsize=[15, 10])
    for i in range(len(keys)):
        dic = results[keys[i]]
        scores = []
        for label in labels:
            scores.append(dic[label])
        plt.bar(X + 0.15*i, scores, color = colors[i], width = 0.5)

#     plt.legend(['2017 trainset', '2018 trainset', 'combined trainset'])
    plt.legend(['Benign 2018'])
    # Overiding the x axis with the country names
    plt.xticks([i + 0.15 for i in range(len(attack_list))], attacks)
    for ticklabel, tickcolor in zip(plt.gca().get_xticklabels(), attack_color):
        ticklabel.set_color(tickcolor)


#     plt.xticks([i + 0.15 for i in range(len(attack_list))], year)
    plt.title("Auc scores for benign sets of 2018", fontsize=15)
    # Namimg the x and y axis
    plt.xlabel('Attacks',fontsize = 20)
    plt.ylabel('Auc', fontsize=20)
    plt.xticks(rotation = 45)
    # Saving the plot as a 'png'
    # plt.savefig('4BarPlot.png')
    # Displaying the bar plot
    plt.show()
    
#####m No mixing, no sampling
file_name = "/data/vantran/Arjun/arjun/dist-network-ml-arjun/output/CIC-IDS-2017/unsupervised/nfstream/2018_KDE_full.txt"
string = read_file(file_name)
keys, results = non_sampling_scores(string)
plot_graph(keys, results)

###### Comparing between different full training set
file_name = "/data/vantran/Arjun/arjun/dist-network-ml-arjun/output/CIC-IDS-2017/unsupervised/nfstream/2018_KDE_full.txt"
string = read_file(file_name)
keys, results = non_sampling_scores(string)
dic_2018 = results[keys[0]]

file_name = "/data/vantran/Arjun/arjun/dist-network-ml-arjun/output/CIC-IDS-2017/unsupervised/nfstream/2017_KDE_full.txt"
string = read_file(file_name)
keys, results = non_sampling_scores(string)
dic_2017 = results[keys[0]]

file_name = "/data/vantran/Arjun/arjun/dist-network-ml-arjun/output/CIC-IDS-2017/unsupervised/nfstream/2017_2018_KDE_full.txt"
string = read_file(file_name)
keys, results = non_sampling_scores(string)
dic_2017_2018 = results[keys[0]]

colors = ['g','blue','orange','red','purple', 'grey','yellow','brown','black', 'pink']
attack_list = ['CIC-IDS-2017_Tuesday_FTP-Patator.csv', 'CIC-IDS-2017_Thursday_Infiltration.csv', 'CIC-IDS-2017_Friday_Bot.csv', 'CIC-IDS-2017_Friday_DDoS.csv', 'CIC-IDS-2017_Thursday_WebAttack.csv', 'CIC-IDS-2017_Tuesday_SSH-Patator.csv', 'CIC-IDS-2017_Friday_Portscan.csv', 'Friday-16-02-2018/DoS_Hulkonly.csv', 'Thursday-15-02-2018/DoS-Slowlorisonly.csv', 'Thursday-15-02-2018/DoS-GoldenEyeonly.csv', 'Wednesday-14-02-2018/SSH-BruteForceonly.csv']
attack_color = ['black','black','black','black','black','black','black','blue','blue','blue','blue']
attacks = ['FTP-Patator\n2017', 'Infiltration\n2017','Bot\n2017','DDoS\n2017','WebAttack\n2017','SSH-Patator\n2017',
          'Portscan\n2017','DoS_Hulk\n2018','DoS-Slowloris\n2018','DoS-GoldenEye\n2018','SSH-BruteForce\n2018']
X = np.arange(len(attack_list))
plt.figure(figsize=[15, 10])
scores_2017 = []
scores_2018 = []
scores_mix = []
for label in attack_list:
    scores_2017.append(dic_2017[label])
    scores_2018.append(dic_2018[label])
    scores_mix.append(dic_2017_2018[label])
    
plt.bar(X, scores_2017, color = colors[0], width = 0.2)
plt.bar(X+0.2, scores_2018, color = colors[1], width = 0.2)
plt.bar(X+0.4, scores_mix, color = colors[2], width = 0.2)

#     plt.legend(['2017 trainset', '2018 trainset', 'combined trainset'])
plt.legend(["train 2017","train 2018", "train 2017&2018"])
# Overiding the x axis with the country names
plt.xticks([i + 0.3 for i in range(len(attack_list))], attacks)
for ticklabel, tickcolor in zip(plt.gca().get_xticklabels(), attack_color):
    ticklabel.set_color(tickcolor)


#     plt.xticks([i + 0.15 for i in range(len(attack_list))], year)
plt.title("Auc scores comparison for different full train sets", fontsize=15)
# Namimg the x and y axis
plt.xlabel('Attacks',fontsize = 20)
plt.ylabel('Auc', fontsize=20)
plt.xticks(rotation = 45)
# Saving the plot as a 'png'
# plt.savefig('4BarPlot.png')
# Displaying the bar plot
plt.show()

####### Comparing between sampling and non-sampling
file_name = "/data/vantran/Arjun/arjun/dist-network-ml-arjun/output/CIC-IDS-2017/unsupervised/nfstream/2018_KDE_sampling.txt"
string = read_file(file_name)
keys, results = non_sampling_scores(string)
dic_sampling = results[keys[0]]


file_name = "/data/vantran/Arjun/arjun/dist-network-ml-arjun/output/CIC-IDS-2017/unsupervised/nfstream/2018_KDE_full.txt"
string = read_file(file_name)
keys, results = non_sampling_scores(string)
dic_full = results[keys[0]]


colors = ['g','blue','orange','red','purple', 'grey','yellow','brown','black', 'pink']
attack_list = ['CIC-IDS-2017_Tuesday_FTP-Patator.csv', 'CIC-IDS-2017_Thursday_Infiltration.csv', 'CIC-IDS-2017_Friday_Bot.csv', 'CIC-IDS-2017_Friday_DDoS.csv', 'CIC-IDS-2017_Thursday_WebAttack.csv', 'CIC-IDS-2017_Tuesday_SSH-Patator.csv', 'CIC-IDS-2017_Friday_Portscan.csv', 'Friday-16-02-2018/DoS_Hulkonly.csv', 'Thursday-15-02-2018/DoS-Slowlorisonly.csv', 'Thursday-15-02-2018/DoS-GoldenEyeonly.csv', 'Wednesday-14-02-2018/SSH-BruteForceonly.csv']
attack_color = ['black','black','black','black','black','black','black','blue','blue','blue','blue']
attacks = ['FTP-Patator\n2017', 'Infiltration\n2017','Bot\n2017','DDoS\n2017','WebAttack\n2017','SSH-Patator\n2017',
          'Portscan\n2017','DoS_Hulk\n2018','DoS-Slowloris\n2018','DoS-GoldenEye\n2018','SSH-BruteForce\n2018']
plt.figure(figsize=[15, 10])
scores_sampling = []
scores_full = []
for label in attack_list:
    scores_sampling.append(dic_sampling[label])
    scores_full.append(dic_full[label])
    
    
plt.bar(X, scores_sampling, color = colors[0], width = 0.3)
plt.bar(X+0.3, scores_full, color = colors[1], width = 0.3)

#     plt.legend(['2017 trainset', '2018 trainset', 'combined trainset'])
plt.legend(["sampling","full"])
# Overiding the x axis with the country names
plt.xticks([i + 0.3 for i in range(len(attack_list))], attacks)
for ticklabel, tickcolor in zip(plt.gca().get_xticklabels(), attack_color):
    ticklabel.set_color(tickcolor)


#     plt.xticks([i + 0.15 for i in range(len(attack_list))], year)
plt.title("Auc scores comparison for sampling versus non sampling for 2018 train set", fontsize=15)
# Namimg the x and y axis
plt.xlabel('Attacks',fontsize = 20)
plt.ylabel('Auc', fontsize=20)
plt.xticks(rotation = 45)
# Saving the plot as a 'png'
# plt.savefig('4BarPlot.png')
# Displaying the bar plot
plt.show()




##### Comparison for different train days
file_name = "/data/vantran/Arjun/arjun/dist-network-ml-arjun/output/CIC-IDS-2017/unsupervised/nfstream/2018_train_days_KDE_sample1.txt"
string = read_file(file_name)
keys, results = non_sampling_scores(string)
plot_graph(keys, results)

file_name = "/data/vantran/Arjun/arjun/dist-network-ml-arjun/output/CIC-IDS-2017/unsupervised/nfstream/2017train_KDE.txt"
string = read_file(file_name)
keys, results = non_sampling_scores(string)

plot_graph( keys, results)
def sampling_scores(string):
   
    strings = string.split("\n")
    big_dict = {}
    for string in strings:
        if string != "":
            dic = eval(string)
            train = "-".join(dic["benign_sources"])
            if "sample_level" not in dic.keys():
                sample_level = 1
            else:
                sample_level = dic["sample_level"]
                
            test = "-".join(dic["mal_sources"])
            score = dic["auc"][0]
            if train not in big_dict.keys():
                big_dict[train]={}

            sub_dic = big_dict[train]
            if sample_level not in sub_dic.keys():
                sub_dic[sample_level]={}
            sub_dic[sample_level][test]=score

    keys = list(big_dict.keys())

    return keys, big_dict
    
# Declaring the figure or the plot (y, x) or (width, height)
attack_list = ['CIC-IDS-2017_Tuesday_FTP-Patator.csv', 'CIC-IDS-2017_Thursday_Infiltration.csv', 'CIC-IDS-2017_Friday_Bot.csv', 'CIC-IDS-2017_Friday_DDoS.csv', 'CIC-IDS-2017_Thursday_WebAttack.csv', 'CIC-IDS-2017_Tuesday_SSH-Patator.csv', 'CIC-IDS-2017_Friday_Portscan.csv', 'Friday-16-02-2018/DoS_Hulkonly.csv', 'Thursday-15-02-2018/DoS-Slowlorisonly.csv', 'Thursday-15-02-2018/DoS-GoldenEyeonly.csv', 'Wednesday-14-02-2018/SSH-BruteForceonly.csv']
attack_color = ['black','black','black','black','black','black','black','blue','blue','blue','blue']
attacks = ['FTP-Patator\n2017', 'Infiltration\n2017','Bot\n2017','DDoS\n2017','WebAttack\n2017','SSH-Patator\n2017',
          'Portscan\n2017','DoS_Hulk\n2018','DoS-Slowloris\n2018','DoS-GoldenEye\n2018','SSH-BruteForce\n2018']
X = np.arange(len(attack_list))
def plot_graph_sampling(keys, big_dict):
    colors = ['g','blue','orange','red','purple', 'grey','yellow','brown','black', 'pink']
    plt.figure(figsize=[25, 10])
#     init_attack_list = False
    

    for key in keys:
        dic = big_dict[key]
        
        labels = sorted(list(dic.keys()))
#         if not init_attack_list:
#             attack_list = list(dic[labels[0]].keys())
#             
#             init_attack_list = True 

        for i in range(len(labels)): 
            sub_dic = dic[labels[i]]
            score = []
            for attack in attack_list:
                score.append(sub_dic[attack])
            plt.bar(X + 0.07*i, score, color = colors[i], width = 0.07)

        plt.legend(labels)
 
        # Overiding the x axis with the country names
        plt.xticks([i + 0.07 for i in range(len(attack_list))], attacks)
        for ticklabel, tickcolor in zip(plt.gca().get_xticklabels(), attack_color):
            ticklabel.set_color(tickcolor)
        plt.title("Auc scores for anomaly detection with sampling for 2017 train set", fontsize = 15)
        # Namimg the x and y axis
        plt.xlabel('Attacks', fontsize=20)
        plt.ylabel('Auc', fontsize=20)
        plt.xticks(rotation=45)

        # Saving the plot as a 'png'
        # plt.savefig('4BarPlot.png')
        # Displaying the bar plot
        plt.show()
###### Comparison for sampling rate
file_name = "/data/vantran/Arjun/arjun/dist-network-ml-arjun/output/CIC-IDS-2017/unsupervised/nfstream/2017_train_KDE_sampling.txt"
string = read_file(file_name)
keys, results = sampling_scores(string)




plot_graph_sampling(keys, results)
big_dict_2 = {}
for string in sampling:
    if string != "":
        dic = eval(string)


        train = "-".join(dic["benign_sources"])
        test = "-".join(dic["mal_sources"])
        score = dic["auc"][0]
        if train not in big_dict_2.keys():
            big_dict_2[train]={}
       
        sub_dic = big_dict_2[train]
        sub_dic[test]=score
keys = list(big_dict_2.keys())
print(keys)
labels = list(big_dict_2[keys[0]].keys())
year_2017 = []
dict_2017 = big_dict_1["CIC-IDS-2017_Monday_Benign.csv"]
year_2018 = []
dict_2018 = big_dict_2["Wednesday-14-02-2018/Benignonly.csv"]
combined_year = []
dict_combined = big_dict_2["CIC-IDS-2017_Monday_Benign.csv-Wednesday-14-02-2018/Benignonly.csv"]
for label in labels:
    year_2017.append(dict_2017[label])
    year_2018.append(dict_2018[label])
    if label in dict_combined.keys():
        combined_year.append(dict_combined[label])
    else:
        combined_year.append(0)
# Declaring the figure or the plot (y, x) or (width, height)
plt.figure(figsize=[15, 10])
X = np.arange(len(year_2017))
plt.bar(X, year_2017, color = 'black', width = 0.25)
plt.bar(X + 0.25, year_2018, color = 'g', width = 0.25)
plt.bar(X + 0.5, combined_year, color = 'blue', width = 0.25)
plt.legend(['2017 trainset', '2018 trainset', 'combined trainset'])
# Overiding the x axis with the country names
plt.xticks([i + 0.25 for i in range(len(labels))], labels)
plt.title("Accuracy scores for anomaly detection sampling")
# Namimg the x and y axis
plt.xlabel('Attacks')
plt.ylabel('Accuracy')
plt.xticks(rotation=90)
# Saving the plot as a 'png'
# plt.savefig('4BarPlot.png')
# Displaying the bar plot
plt.show()

import pandas as pd
filename = "/data/arjun/datasets/CIC-IDS-2018/nfstream/Wednesday-14-02-2018/Benignonly.csv"
df = pd.read_csv(filename)
