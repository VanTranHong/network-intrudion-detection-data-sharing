#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[62]:


folder = "/data/vantran/Arjun/nds/IoT-data/IoT-CVS/"
sub_folder = "CTU-IoT-Malware-Capture-34-1/"
file_name1 = folder+sub_folder+"2018-12-21-15-50-14-192.168.1.195.csv"
df = pd.read_csv(file_name1, index_col=None, header=0)
print(df.shape)
file_name2 = folder+sub_folder+"label.csv"
df = pd.read_csv(file_name2, index_col=None, header=0)
print(df.shape)


# In[63]:


df_strat = pd.read_csv(file_name2)
df_nfstream = pd.read_csv(file_name1)
df_nfstream_copy = df_nfstream.copy(deep = True)


# In[64]:


df_nfstream_copy['src_ip'] = df_nfstream['dst_ip']
df_nfstream_copy['dst_ip'] = df_nfstream['src_ip']
df_nfstream_copy['src_port'] = df_nfstream['dst_port']
df_nfstream_copy['dst_port'] = df_nfstream['src_port']
df_nfstream = pd.concat([df_nfstream,df_nfstream_copy])


# In[65]:


print(df_nfstream.columns, df_strat.columns)


# In[66]:


print(df_nfstream.shape)


# In[67]:


print(df_strat.shape)


# In[54]:


df_strat


# In[55]:


df_strat_subset = df_strat[["ts", 'id.orig_h', 'id.orig_p', 'id.resp_h', 'id.resp_p', 'label', 'detailed-label','duration']]


# In[56]:


strat_on = ['id.orig_h', 'id.orig_p', 'id.resp_h', 'id.resp_p']
nfstream_on = ["src_ip", "src_port", "dst_ip", "dst_port"]
df_merge = pd.merge(df_nfstream, df_strat_subset, left_on = nfstream_on, right_on=strat_on)
df_merge.shape


# In[57]:


def cast_float(x):
    try:
        return float(x)
    except:
        return 0
    
def is_overlapping(x):
    s1 = x['bidirectional_first_seen_ms']/1000
    e1 = x['bidirectional_last_seen_ms']/1000
    s2 = x['ts']
    e2 = x['te']
    if (s1 >= s2) and (s1 <= e2):
        return True
    elif (s2 >= s1) and (s2 <= e1):
        return True
    return False
    
    
df_merge['ts'] = df_merge['ts'].astype(float)
df_merge['duration'] = df_merge["duration"].apply(cast_float)

df_merge['te'] = df_merge["ts"] + df_merge["duration"]

df_merge_1 = df_merge[df_merge.apply(is_overlapping, axis=1)]

print(df_merge_1.shape)


# In[58]:


df_merge_1.head()


# In[59]:


df_merge_1.columns


# In[60]:


final = df_merge_1[['src_ip', 'src_mac','src_oui',
       'src_port', 'dst_ip', 'dst_mac', 'dst_oui', 'dst_port','protocol','bidirectional_first_seen_ms',
       'bidirectional_last_seen_ms', 'bidirectional_duration_ms',
       'bidirectional_packets', 'bidirectional_bytes', 'src2dst_first_seen_ms',
       'src2dst_last_seen_ms', 'src2dst_duration_ms', 'src2dst_packets',
       'src2dst_bytes', 'dst2src_first_seen_ms', 'dst2src_last_seen_ms',
       'dst2src_duration_ms', 'dst2src_packets', 'dst2src_bytes', 'ts','label', 'detailed-label','duration']]


# In[61]:


final.to_csv(folder+sub_folder+"labeled.csv")


# In[ ]:




