import numpy as np
import pandas as pd
import os
import random


def get_file_name(sources,data_source,data_rep,config):
    """
    there are 2 versions, one is the length of soueces = length of data_sources
    another one is that the length of the sources < length of the data_source
    
    """

    input_files=[]
    if len(sources)==len(data_source):
        for i in range(len(sources)):
            #folder = config['DATA']['input_dir']+'/'+data_source[i]+'/'+data_rep
            folder = config['DATA']['input_dir']+'/'+data_source[i]
            input_files.append(folder+sources[i])
            
    elif len(sources)!=len(data_source):
        #folder = config['DATA']['input_dir']+'/'+data_source[0]+'/'+data_rep
        folder = config['DATA']['input_dir']+'/'+data_source[0]
        for i, input_name in enumerate(sources):
            input_files.append(folder+input_name) 
            


    return input_files

    
    

def read_from_file(data_rep,input_files):
    if data_rep == 'Flowmeter':
        li = []
        print("reading flowmeter data")
        for filename in input_files:
            df = pd.read_csv(filename, index_col=None, header=0)
            # Removing port from features
            df = df.drop(df.columns[[0]], axis=1)
            li.append(df)
        df = pd.concat(li, axis=0, ignore_index=True)
    elif data_rep == 'nfdump':
        li = []
        print("reading nfdump data")
        for filename in input_files:
            df = pd.read_csv(filename, index_col=None, header=0)
            # Removing identifers from features
            df = df.drop(df.columns[[0]], axis=1)
            li.append(df)
        df = pd.concat(li, axis=0, ignore_index=True)
    elif data_rep == 'netml':
        li = []
        print("reading netml data")
        for filename in input_files:
            df = pd.read_csv(filename, index_col=None, header=0)
            # Removing index from features
            df = df.drop(df.columns[[0,1,2,3,4,5,6]], axis=1)
            li.append(df)
        df = pd.concat(li, axis=0, ignore_index=True)
        # Filtering out small flows
        df['flow_size']=df.td*df.packets_per_s
        df=df[df.flow_size>2.0]
        df = df.drop(['flow_size'], axis=1)
    elif data_rep == 'nfstream':
        li = []
    
        for filename in input_files:
    
            df = pd.read_csv(filename, index_col=None, header=0)
            if 'Unnamed: 0.1' in df.columns:
                df = df.drop(['Unnamed: 0.1'], axis=1) 
            if "Unnamed: 0" in df.columns:
                df = df.drop(['Unnamed: 0'], axis=1) 
            li.append(df)
        
      
        df = pd.concat(li, axis=0, ignore_index=True)
        # Filtering out small flows
        df=df[df.bidirectional_packets>2.0]
        
    elif data_source == 'BAS':
        li = []
        print("reading BAS data")
        for filename in input_files:
            df = pd.read_csv(filename, index_col=None, header=0)
            # Removing identifers from features
            df = df[['id','bidirectional_duration_ms',
       'bidirectional_packets', 'bidirectional_bytes', 'src2dst_duration_ms', 'src2dst_packets',
       'src2dst_bytes','dst2src_duration_ms', 'dst2src_packets', 'dst2src_bytes']]
            df['label']=0
            li.append(df)
        df = pd.concat(li, axis=0, ignore_index=True)
    elif data_source == 'CIC-IDS-2018':
        df=pd.read_csv(input_file,delimiter=',')
        df_np=df.to_numpy()
        df_np_perm=df_np[rng.permutation(len(df_np))]
        # Removing port, protocol and timestamp from features
        X=df_np_perm[:,3:-2]
        y=df_np_perm[:,-1]
        
        # Creating labeled data
        y_mod=np.zeros(len(y))
        if sup:
            y_mod[np.where(y==attack_types[i])]=i+1
        else:
            y_mod[np.where(y==attack_types[i])]=1
    elif data_source == 'iot':
        # To-do
        #input_dir = "../../data/benign_attack/nfcapd.*.csv"

        # input_data_file_list = glob.glob(input_dir)
        # li = []
        # print("reading dataframe")
        # for filename in input_data_file_list:
        #         df = pd.read_csv(filename, index_col=None, header=0)
        #         li.append(df)
        # df = pd.concat(li, axis=0, ignore_index=True)
        df = pd.read_csv(args.input_csv, index_col=None, header=0)
        # filter out the last few lines that are aggregate stats and not flow records
        df = df[~pd.isna(df["pr"])]
    benign_sizes = []    
    for dat in li:
        
        if "Benign" in dat["Label"].unique():
            benign_sizes.append(len(dat))
    sample_size = min(benign_sizes)
    new_li = []
    for dat in li:
        if "Benign" in dat["Label"].unique():
            rng = np.random.default_rng(777)
            train_indices=rng.choice(len(dat),sample_size,replace=False)
            new_dat=dat.iloc[train_indices]
            new_li.append(new_dat)
        else:
            new_li.append(dat)
    df = pd.concat(new_li, axis=0, ignore_index=True)
    for dat in new_li:
        print("shape")
        print(len(dat))
            
        
            

        
    return df, new_li

def data_split(X_clean,y_clean,rng,train_split,sup):
    if sup=='supervised':
        train_len=int(train_split*len(X_clean))
        
        train_indices=rng.choice(len(X_clean),train_len,replace=False)
        test_indices=np.setdiff1d(np.arange(len(X_clean)),train_indices)
        
        X_train=X_clean[train_indices]
        X_test=X_clean[test_indices]
        
        y_train=y_clean[train_indices]
        y_test=y_clean[test_indices]

        train_mal_len=len(np.where(y_train!=0)[0])
        test_mal_len=len(np.where(y_test!=0)[0])

    else:
        benign_indices=np.where(y_clean==0)
        mal_indices=np.where(y_clean!=0)
        
        X_benign=X_clean[benign_indices]
        y_benign=y_clean[benign_indices]
        
        train_len=int(train_split*len(X_benign))
        
        train_indices_benign=rng.choice(len(X_benign),train_len,replace=False)
        test_indices_benign=np.setdiff1d(np.arange(len(X_benign)),train_indices_benign)
        
        X_train=X_benign[train_indices_benign]
        y_train=y_benign[train_indices_benign]
        
        X_test_benign=X_benign[test_indices_benign]
        y_test_benign=y_benign[test_indices_benign]
        
        X_test_mal=X_clean[mal_indices]
        y_test_mal=y_clean[mal_indices]
        
        perm_indices=rng.permutation(len(X_test_benign)+len(X_test_mal))
        
        X_test=np.vstack((X_test_benign,X_test_mal))[perm_indices]
        y_test=np.hstack((y_test_benign,y_test_mal))[perm_indices]
        
        train_mal_len=0
        test_mal_len=len(y_test_mal)
    

    
    return X_train, y_train, X_test, y_test

def filter_data(X, y, attack_types, sup):
    # Mapping 
    y_mod=np.zeros(len(y))
    for j in range(len(attack_types)):
        print('Attack %s mapped to id %s' % (attack_types[j],j+1))
        y_mod[np.where(y==attack_types[j])]=j+1

#     if len(indices_list)>0:        
#         # Adding all benign data
#         indices_list.extend(list(np.where(y_mod==0)[0]))
#         X=X[indices_list]
#         y_mod=y_mod[indices_list]
    if sup=='unsupervised':
        # Collapsing to single malicious class for unsupervised
        y_mod[np.where(y_mod!=0)[0]]=1
    elif sup=='supervised':
        unique_indices=np.unique(y_mod)
        y_sup=np.zeros(len(y_mod))
        for i in range(len(unique_indices)):
            curr_indices=np.where(y_mod==unique_indices[i])
            y_sup[curr_indices]=i
        y_mod=y_sup
    
    return X, y_mod


def read_data_benign(args,config,folder,benign_folders,mal_folders,data_rep,train_split,rng,sup,combined):
    """ This is specifically designed to test benign against benign"""
    if folder =="benign":    
        benign_sources=[]
        benign_sources.extend(args.benign_sources)
        benign_files = get_file_name(benign_sources, benign_folders, args.data_rep, config)
        df, list_of_dfs = read_from_file(data_rep,benign_files)
        print("columns names")
        print(df["Label"].unique())
        if 'Unnamed: 0.1' in df.columns:
        
            df = df.drop(['Unnamed: 0.1'], axis=1) 
        print('Combining all data')
        df_np=df.to_numpy()
        X=df_np[:,0:-1]
        y=df_np[:,-1]
        column_names = list(df.columns)
    else:
        mal_sources=[]
        mal_sources.extend(args.mal_sources)
        mal_files = get_file_name(mal_sources, mal_folders, args.data_rep, config)
        df, list_of_dfs = read_from_file(data_rep,mal_files)
        print("columns names")
        print(df["Label"].unique())
        if 'Unnamed: 0.1' in df.columns:
        
            df = df.drop(['Unnamed: 0.1'], axis=1) 
        print('Combining all data')
        df_np=df.to_numpy()
        X=df_np[:,0:-1]
        y=df_np[:,-1]
        column_names = list(df.columns)
        
        
    return X,y,column_names
    
    
    

    

def read_data(args,config,benign_folders,mal_folders,data_rep,train_split,rng,sup,combined):
    
    if combined:
        benign_sources=[]
        mal_sources=[]
        mal_sources.extend(args.mal_sources)
        benign_sources.extend(args.benign_sources)
        benign_files = get_file_name(benign_sources, benign_folders, args.data_rep, config)
        mal_files = get_file_name(mal_sources, mal_folders, args.data_rep, config)
        
        print("malicious sources")
        print(mal_sources)
        print("benign sources")
        print(benign_sources)
        print("benign folders")
        print(benign_folders)
        print("malicious folders")
        print(mal_folders)
        print("dat_rep")
        print(args.data_rep)
        input_files = benign_files+mal_files


        li = []
        dimensions = []
        
        
        for filename in input_files:
            df = pd.read_csv(filename, index_col=None, header=0)
            # Removing port from features
            if "Unnamed: 0" in df.columns:

                df = df.drop(["Unnamed: 0"], axis=1)
            if "Unnamed: 0.1" in df.columns:
                df = df.drop(["Unnamed: 0.1"], axis=1)
            li.append(df)
            dimensions.append(df.shape[0])
#         min_dim = min(dimensions)
#         li_shuffled = []
#         for df in li:
#             df_shuffled = list(range(df.shape[0]))
#             random.shuffle(df_shuffled)
#             df_shuffled=df[:min_dim]
#             li_shuffled.append(df_shuffled)

            
            
        
        
        df = pd.concat(li, axis=0, ignore_index=True)
        print(df.columns)

#        df, list_of_dfs = read_from_file(data_rep,input_files)
        assert isinstance(df, pd.DataFrame), "df needs to be a pd.DataFrame"
        df.dropna(inplace=True)
        indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
        df = df[indices_to_keep]
        column_names = list(df.columns)
        print("columns names")
        print(column_names)
        print(df["label"].unique())
        
           
#        print('Combining all data')
#        df_np=df.to_numpy()

#        X=df_np[:,0:-1]
#        y=df_np[:,-1]
        print("Columns: ")
        print(df.columns)
        X = df[['protocol',
       'bidirectional_first_seen_ms', 'bidirectional_last_seen_ms',
       'bidirectional_duration_ms', 'bidirectional_packets',
       'bidirectional_bytes', 'src2dst_first_seen_ms', 'src2dst_last_seen_ms',
       'src2dst_duration_ms', 'src2dst_packets', 'src2dst_bytes',
       'dst2src_first_seen_ms', 'dst2src_last_seen_ms', 'dst2src_duration_ms',
       'dst2src_packets', 'dst2src_bytes', 'ts',
       'duration']].to_numpy()
        y=df["label"].to_numpy()

        
        y_mod=np.zeros(len(y))
        if args.mal_sources is not None:
            X, y_mod=filter_data(X,y,args.attack_types,sup)


        X_train, y_train, X_test, y_test = data_split(X,y_mod,rng,train_split,sup)
     
        
    else:
#         benign_sources=[]
#         mal_sources=[]
#         mal_sources.extend(args.mal_sources)
#         benign_sources.extend(args.benign_sources)
        train_input_files=get_file_name(benign_sources, benign_folders, args.data_rep,config)
        train_df, list_of_train_dfs = read_from_file(data_rep, train_input_files)
        
        test_input_files=get_file_name(mal_sources, mal_folders, args.data_rep, config)
        test_df, list_of_test_dfs = read_from_file(data_rep,test_input_files)
    
        train_df_np=train_df.to_numpy()

        X_train=train_df_np[:,0:-1]
        y_train=train_df_np[:,-1]
        
        X_train,y_train =filter_data(X_train,y_train,args.attack_types,sup)
    
        test_df_np=test_df.to_numpy()
        test_df_np_perm=test_df_np[rng.permutation(len(test_df_np))]

        X_test=test_df_np_perm[:,0:-1]
        y_test=test_df_np_perm[:,-1]
        column_names = list(df.columns)
        
        X_test,y_test =filter_data(X_test,y_test,args.attack_types,sup)

    
    return X_train, y_train, X_test, y_test, column_names
       
