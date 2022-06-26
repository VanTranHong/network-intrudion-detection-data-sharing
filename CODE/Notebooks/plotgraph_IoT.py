import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import statistics as stat

def read_file(file_name):
    f = open(file_name, "r")
    string = f.read()
    return string
def get_shortform(string):
    return "-".join(string.split("/")[0].split("-")[-2:])
    
def non_sampling_scores(string):
    strings = string.split("\n")
    big_dict = {}
    for string in strings:
        if string != "":
            dic = eval(string)
            sample_level = dic["sample_level"]
            shortform_benign=[get_shortform(benign) for benign in dic["benign_sources"]]
            shortform_benign.sort()
            shortform_malicious = [get_shortform(mal) for mal in dic["mal_sources"]]
            shortform_malicious.sort()
            train = "&".join(shortform_benign)
            test = "&".join(shortform_malicious)
            score=dic["auc"][0]
            
            if test not in big_dict.keys():
                big_dict[test]={}
    
            sub_dict = big_dict[test]
            if str(sample_level) not in sub_dict.keys():
                sub_dict[str(sample_level)]={}
            sub_sub_dict = sub_dict[str(sample_level)]
            len_train = len(shortform_benign)
            if str(len_train) not in sub_sub_dict.keys():
                sub_sub_dict[str(len_train)]={}
            sssd = sub_sub_dict[str(len_train)]
            sssd[train]=score
    keys = list(big_dict.keys())
    return keys, big_dict
file_name = "/data/vantran/Arjun/arjun/dist-network-ml-arjun/output/IoT/unsupervised/KDE.txt"
string = read_file(file_name)
keys, results_equal = non_sampling_scores(string)

file_name = "/data/vantran/Arjun/arjun/dist-network-ml-arjun/output/IoT/unsupervised/KDE_notequalsize.txt"
string = read_file(file_name)
keys, results_original = non_sampling_scores(string)
###### Comparing between making trainsize equal and not equal
test_3_1_equal = results_equal["3-1"]["1.0"]
test_3_1_original = results_original["3-1"]["1.0"]
test_34_1_equal = results_equal["34-1"]["1.0"]
test_34_1_original = results_original["34-1"]["1.0"]


the_keys_3_1 = []
val_34_1_equal = []
val_34_1_original = []
for k in test_3_1_equal.keys():
    sub_dic = test_3_1_equal[k]
    for key in sub_dic.keys():
        the_keys_3_1.append(key)
#         val_3_1_equal.append(sub_dic[key])
#         val_3_1_original.append(test_3_1_original[k][key])
sorted(the_keys_3_1,key=len, reverse = True)
the_keys_3_1 = the_keys_3_1[-1::-1]
the_keys_3_1

# for k in the_keys_34_1:
#     for key in test_34_1_original.keys():
#         if k in test_34_1_original[key].keys():
#             val_34_1_equal.append(test_34_1_equal[key][k])
#             val_34_1_original.append(test_34_1_original[key][k])
# # print(val_3_1_equal)
# # print(val_3_1_original)

# colors = ['g','blue','orange','red','purple', 'grey','yellow','brown','black', 'pink']
# X = [i for i in range(len(val_3_1_equal))]
# plt.bar(X , val_34_1_equal, color = colors[0], width = 0.3)
# plt.bar([x+0.3 for x in X] , val_34_1_original, color = colors[1], width = 0.3)
# plt.legend(["Equal train size", "Not modified trainsize"])
# plt.xticks(X, the_keys_34_1, fontsize=15, rotation=90)
# plt.yticks(fontsize=15)
# plt.xlabel('Train set',fontsize = 20)
# plt.ylabel('Auc', fontsize=20)
# plt.title("Auc scores when using different trainsets on 34-1 testset", fontsize=15)
# plt.show()  

# print(the_keys_34_1)
            
            
test_3_1__1_0 = results_equal["3-1"]["1.0"]
test_3_1__0_8 = results_equal["3-1"]["0.8"]
test_3_1__0_6 = results_equal["3-1"]["0.6"]
val_1_0=[]
val_0_8=[]
val_0_6=[]



the_keys_3_1 = []

for k in test_3_1__1_0.keys():
    sub_dic = test_3_1__1_0[k]
    for key in sub_dic.keys():
        the_keys_3_1.append(key)

sorted(the_keys_3_1,key=len, reverse = True)
the_keys_3_1 = the_keys_3_1[-1::-1]
the_keys_3_1

for k in the_keys_3_1:
    for key in test_3_1__1_0.keys():
        if k in test_3_1__1_0[key].keys():
            val_1_0.append(test_3_1__1_0[key][k])
            val_0_8.append(test_3_1__0_8[key][k])
            val_0_6.append(test_3_1__0_6[key][k])
            


colors = ['g','blue','orange','red','purple', 'grey','yellow','brown','black', 'pink']
X = [i for i in range(len(the_keys_3_1))]
plt.bar(X , val_1_0, color = colors[0], width = 0.25)
plt.bar([x+0.25 for x in X] , val_0_8, color = colors[1], width = 0.25)
plt.bar([x+0.5 for x in X] , val_0_6, color = colors[2], width = 0.25)
plt.legend(["1.0", "0.8","0.6"])
plt.xticks(X, the_keys_3_1, fontsize=15, rotation=90)
plt.yticks(fontsize=15)
plt.xlabel('Train set',fontsize = 20)
plt.ylabel('Auc', fontsize=20)
plt.title("Auc scores with different sampling level of trainsize on 3-1 testset", fontsize=15)
plt.show()        
file_name = "/data/vantran/Arjun/arjun/dist-network-ml-arjun/output/IoT/unsupervised/KDE_notequalsize.txt"
string = read_file(file_name)
keys, results = non_sampling_scores(string)
print(results)


###### Different test set
colors = ['g','blue','orange','red','purple', 'grey','yellow','brown','black', 'pink']
testset3_1 = results["3-1"]
testset34_1 = results["34-1"]
### one train set, full train points, different testset
plt.figure(figsize=[15, 10])
one_ts_full_3_1 = testset3_1["1.0"]["1"]
one_ts_full_34_1 = testset34_1["1.0"]["1"]

keys = list(set(one_ts_full_3_1.keys()).union(set(one_ts_full_34_1.keys()))) 
X = [0, 1.5]
val_3_1 = []
val_34_1 = []
for i in range(len(keys)):
    k = keys[i]
    val_3_1 = 0
    val_34_1 = 0
    if k in one_ts_full_3_1.keys():
        val_3_1=one_ts_full_3_1[k]
    if k in one_ts_full_34_1.keys():
        val_34_1=one_ts_full_34_1[k]
    plt.bar([x+0.15*i for x in X] , [val_3_1, val_34_1], color = colors[i], width = 0.15)
plt.legend(keys)
plt.xticks([0,1.5], ["3_1 test set","34_1 test set"], fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Test set',fontsize = 20)
plt.ylabel('Auc', fontsize=20)
plt.title("Auc scores for different test sets using single train set full size", fontsize=15)
plt.show()
### one train set, full train points, different testset
plt.figure(figsize=[15, 10])
two_ts_full_3_1 = testset3_1["1.0"]["2"]
two_ts_full_34_1 = testset34_1["1.0"]["2"]

keys = list(set(two_ts_full_3_1.keys()).union(set(two_ts_full_34_1.keys()))) 
X = [0, 2]
val_3_1 = []
val_34_1 = []
for i in range(len(keys)):
    k = keys[i]
    val_3_1 = 0
    val_34_1 = 0
    if k in two_ts_full_3_1.keys():
        val_3_1=one_ts_full_3_1[k]
    if k in two_ts_full_34_1.keys():
        val_34_1=one_ts_full_34_1[k]
    plt.bar([x+0.1*i for x in X] , [val_3_1, val_34_1], color = colors[i], width = 0.11)
plt.legend(keys)
plt.xticks([0,2], ["3_1 test set","34_1 test set"], fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Test set',fontsize = 20)
plt.ylabel('Auc', fontsize=20)
plt.title("Auc scores for different test sets using 2 train sets full size", fontsize=15)
plt.show()
### one train set, full train points, different testset
plt.figure(figsize=[15, 10])
three_ts_full_3_1 = testset3_1["1.0"]["3"]
three_ts_full_34_1 = testset34_1["1.0"]["3"]

keys = list(set(three_ts_full_3_1.keys()).union(set(three_ts_full_34_1.keys()))) 
X = [0, 1.5]
val_3_1 = []
val_34_1 = []
for i in range(len(keys)):
    k = keys[i]
    val_3_1 = 0
    val_34_1 = 0
    if k in three_ts_full_3_1.keys():
        val_3_1=one_ts_full_3_1[k]
    if k in three_ts_full_34_1.keys():
        val_34_1=one_ts_full_34_1[k]
    plt.bar([x+0.1*i for x in X] , [val_3_1, val_34_1], color = colors[i], width = 0.11)
plt.legend(keys)
plt.xticks([0,1.5], ["3_1 test set","34_1 test set"], fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Test set',fontsize = 20)
plt.ylabel('Auc', fontsize=20)
plt.title("Auc scores for different test sets using 3 train sets full size", fontsize=15)
plt.show()
### one train set, full train points, different testset
plt.figure(figsize=[15, 10])
four_ts_full_3_1 = testset3_1["1.0"]["4"]
four_ts_full_34_1 = testset34_1["1.0"]["4"]

keys = list(set(four_ts_full_3_1.keys()).union(set(four_ts_full_34_1.keys()))) 
X = [0, 1]
val_3_1 = []
val_34_1 = []
for i in range(len(keys)):
    k = keys[i]
    val_3_1 = 0
    val_34_1 = 0
    if k in four_ts_full_3_1.keys():
        val_3_1=one_ts_full_3_1[k]
    if k in four_ts_full_34_1.keys():
        val_34_1=one_ts_full_34_1[k]
    plt.bar([x+0.1*i for x in X] , [val_3_1, val_34_1], color = colors[i], width = 0.11)
plt.legend(keys)
plt.xticks([0,1], ["3_1 test set","34_1 test set"], fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Test set',fontsize = 20)
plt.ylabel('Auc', fontsize=20)
plt.title("Auc scores for different test sets using 4 train sets full size", fontsize=15)
plt.show()

##### For testset 3-1
### one train set, full train points, different testset

### the train sets are 1-1, 20-1, 21-1, 34-1


##### Different ways trainset 1-1 are used

plt.figure(figsize=[15, 10])
one = testset3_1["1.0"]["1"]["1-1"]

plt.bar([0] , [one], color = colors[0], width = 0.09)
plt.xticks([0,1,2,3], [1,2,3,4], fontsize=15)


two = testset3_1["1.0"]["2"]
keys = list(two.keys())
included_keys=[]
for k in keys:
    k_ = k.split("&")
    if "1-1" in k_:
        included_keys.append(k)
X = [1+0.1*i for i in range(len(included_keys))]
plt.bar(X , [two[k] for k in included_keys], color = colors[1], width = 0.09)

# plt.xticks(X , included_keys, fontsize=15, minor = True)

three = testset3_1["1.0"]["3"]
keys = list(three.keys())
included_keys=[]
for k in keys:
    k_ = k.split("&")
    if "1-1" in k_:
        included_keys.append(k)
X = [2+0.1*i for i in range(len(included_keys))]
plt.bar(X , [three[k] for k in included_keys], color = colors[2], width = 0.09)


four = testset3_1["1.0"]["4"]
keys = list(four.keys())
included_keys=[]
for k in keys:
    k_ = k.split("&")
    if "1-1" in k_:
        included_keys.append(k)
X = [3+0.1*i for i in range(len(included_keys))]
plt.bar(X , [four[k] for k in included_keys], color = colors[3], width = 0.09)
plt.legend(["1 train set","2 train sets","3 train sets","4 train sets"])


# three_ts_full_3_1 = testset3_1["1.0"]["3"]
# keys = list(three_ts_full_3_1.keys())
# X = [3+0.15*i for i in range(len(keys))]
# plt.bar(X , [three_ts_full_3_1[k] for k in keys], color = colors[2], width = 0.15)

# four_ts_full_3_1 = testset3_1["1.0"]["4"]
# keys = list(four_ts_full_3_1.keys())
# X = [4.5+0.15*i for i in range(len(keys))]
# plt.bar(X , [four_ts_full_3_1[k] for k in keys], color = colors[3], width = 0.15)
# # plt.legend(keys)
# # plt.xticks([0,1], ["3_1 test set","34_1 test set"], fontsize=15)
# # plt.yticks(fontsize=15)
plt.xlabel('Number of train sets',fontsize = 20)
# plt.ylabel('Auc', fontsize=20)
# # plt.title("Auc scores for different test sets using 4 train sets full size", fontsize=15)
plt.show()
### one train set, full train points, different testset

### the train sets are 1-1, 20-1, 21-1, 34-1


##### Different ways trainset 1-1 are used
fig, ax = plt.subplots()


trainset = "21-1"
one = testset34_1["1.0"]["1"][trainset]
pps = ax.bar([0] , [one], color = colors[0], width = 0.19)
for p in pps:
    height = p.get_height()
    ax.text(x=p.get_x() + p.get_width() / 2, y=height/2,
    s="{}".format(trainset),
    ha='center', rotation=90, color ="white")


two = testset34_1["1.0"]["2"]
keys = list(two.keys())
included_keys=[]
for k in keys:
    k_ = k.split("&")
    if trainset in k_:
        included_keys.append(k)
X = [1+0.2*i for i in range(len(included_keys))]
pps = ax.bar(X , [two[k] for k in included_keys], color = colors[1], width = 0.19)
for i in range(len(pps)):
    p=pps[i]
    height = p.get_height()
    ax.text(x=p.get_x() + p.get_width() / 2, y=height/4,
    s="{}".format(included_keys[i]),
    ha='center', rotation=90, color ="white")

# # plt.xticks(X , included_keys, fontsize=15, minor = True)

three = testset34_1["1.0"]["3"]
keys = list(three.keys())
included_keys=[]
for k in keys:
    k_ = k.split("&")
    if trainset in k_:
        included_keys.append(k)
X = [2+0.2*i for i in range(len(included_keys))]
pps = ax.bar(X , [three[k] for k in included_keys], color = colors[2], width = 0.19)
for i in range(len(pps)):
    p=pps[i]
    height = p.get_height()
    ax.text(x=p.get_x() + p.get_width() / 2, y=height/4,
    s="{}".format(included_keys[i]),
    ha='center', rotation=90, color ="white")

four = testset34_1["1.0"]["4"]
keys = list(four.keys())
included_keys=[]
for k in keys:
    k_ = k.split("&")
    if trainset in k_:
        included_keys.append(k)
X = [3+0.2*i for i in range(len(included_keys))]
pps = ax.bar(X , [four[k] for k in included_keys], color = colors[3], width = 0.19)
for i in range(len(pps)):
    p=pps[i]
    height = p.get_height()
    ax.text(x=p.get_x() + p.get_width() / 2, y=height/9,
    s="{}".format(included_keys[i]),
    ha='center', rotation=90, color ="white")

    

# ax.legend(["1 train set","2 train sets","3 train sets","4 train sets"])




plt.xticks([0,1,2,3], [1,2,3,4], fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Number of train sets',fontsize = 20)
plt.ylabel('Auc', fontsize=20)
plt.title("Auc scores of test set 34-1 for trainsets that include " + trainset, fontsize=15)
plt.show()


          
