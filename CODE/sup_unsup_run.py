import pathlib
import numpy as np

from sklearn.model_selection import train_test_split, GridSearchCV

from src.netml.ndm.model import MODEL
from src.netml.utils.tool import dump_data, load_data, write_out, output_file_name

from src.netml.utils.data import read_data, read_data_benign

from src.netml.utils.distribution import distribute_dataframe_np

from multiprocessing import Process, Manager
import multiprocessing
import matplotlib.pyplot as plt
import argparse
import configparser

seed = 777

VERBOSITY = 6


def generate_model_sup(args,model_name='SVM'):
    """Generate a supervised model according to the given name.
    current implemented models are "SVM" and "RF"

    Parameters
    ----------
    model_name: string (default is 'SVM')
        the name of the model wants to be generated.

    Returns
    -------
        a MODEL instance

    """

    if model_name == 'SVM':
        from src.netml.ndm.svm import SVM
        params={'loss':'hinge', 'penalty':'l2', 'max_iter': 10000, 'shuffle': True}
        model = SVM(loss=params['loss'], penalty=params['penalty'], max_iter=params['max_iter'], shuffle=params['shuffle'], random_state=seed)
    elif model_name == 'RF':
        from src.netml.ndm.rf import RF
        params={'max_depth': 3}
        model = RF(max_depth=params['max_depth'], random_state=seed)
    else:
        msg = '{model_name} is not implemented yet!'
        raise NotImplementedError(msg)

    model.name = model_name
    return model, params

def generate_model_unsup(args,model_name='GMM'):
    models = []
    
    ##### Van would like to change this to generate a list of models instead of just a model #####
    
    
    
    """Generate a model according to the given name.
    current implemented models are "OCSVM", "GMM",  "IF", "KDE", "PCA" and "AE"

    Parameters
    ----------
    model_name: string (default is 'OCSVM')
        the name of the model wants to be generated.

    Returns
    -------
        a list of MODEL instance

    """
    if model_name == 'OCSVM':
        from src.netml.ndm.ocsvm import OCSVM
        params={'kernel':['linear'],'nu':[0.5]}
        for k in params["kernel"]:
            for n in params["nu"]:
                model = OCSVM(kernel=k, nu=n, random_state=seed)
                model.name = model_name
                models.append(model)
#         grid_search = GridSearchCV(model, params, scoring = "roc_auc")


    elif model_name == 'GMM':
        from src.netml.ndm.gmm import GMM
        params={'n_components': [2],'cov': ['full', "spherical"]}
        for c in params["cov"]:
            for n in params["n_components"]:
                model = GMM(n_components=n, covariance_type=c, random_state=seed, reg_covar=100000)
                model.name = model_name
                models.append(model)
#         grid_search = GridSearchCV(model, params, scoring = "roc_auc")

    elif model_name == 'IF':
        from src.netml.ndm.iforest import IF
        params={'n_estimators': [10,20,30,40,50,60,70,100] }

        for n in params["n_estimators"]:
            model = IF(n_estimators=n, random_state=seed)
            model.name = model_name
            models.append(model)
#         grid_search = GridSearchCV(model, params, scoring = "roc_auc")

    elif model_name == 'PCA':
        from src.netml.ndm.pca import PCA
        params={'n_components': [2,3,5,7] }
        for n in params["n_components"]:
            model = PCA(n_components=n, random_state=seed)
            model.name = model_name
            models.append(model)
#         grid_search = GridSearchCV(model, params, scoring = "roc_auc")


    elif model_name == 'KDE':
        from src.netml.ndm.kde import KDE
        params={'kernel': ['gaussian'],'bandwidth': [0.2, 0.4,0.6,0.8, 1.0, 1.5, 2.0]}
        for k in params["kernel"]:
            for b in params["bandwidth"]:
                model = KDE(kernel=k, bandwidth=b, random_state=seed)
                model.name = model_name
                models.append(model)
#         model = KDE(random_state=seed)
#         grid_search = GridSearchCV(model, params, scoring = "roc_auc")


    elif model_name == 'AE':
        from src.netml.ndm.ae import AE
        params={'epochs': [100],'batch_size': [128], 'hid_dim': [5], 'lat_dim': [5]}

        for e in params["epochs"]:
            for b in params["batch_size"]:
                for h in params["hid_dim"]:
                    for l in params["lat_dim"]:
                        model = AE(epochs=e, batch_size=b, random_state=seed, verbose=VERBOSITY, hid_dim=h, lat_dim=l)
                        model.name = model_name
                        models.append(model)
#         grid_search = GridSearchCV(model, params, scoring = "roc_auc")

        
    else:
        msg = '{model_name} is not implemented yet!'
        raise NotImplementedError(msg)

    

    return models,  params





def model_run(args, alg_type, data_source, seed, i, X_train, y_train, X_test, y_test, ben_only_flag, return_dict):
    print('Running training for data split %s' % i)
    # model_name in ['OCSVM', 'KDE','IF', 'AE', 'GMM', 'PCA'] if unsupervised; ['SVM,'RF'] otherwise
    model_name = args.model_name
    ndms = []
    scores = []
    train_time = []
    test_time = []
    
   
    if alg_type=='unsupervised':
#         # create detection model
        print('Running unsupervised learning with model %s' % model_name)
        models, params = generate_model_unsup(args,model_name)
        print("number of models", len(models))
        
        
        for model in models:
            
            ndm = MODEL(model, score_metric='auc', verbose=10, random_state=seed)
            ndm.train(X_train)
            if ben_only_flag:
                ndm.soft_test(X_test)
            else:
                ndm.test(X_test, y_test)    
            ndms.append(ndm)
            scores.append(ndm.score)
        print(" scores are")
        print(scores)
        best_ndm_index = np.argsort(scores)[-1]
        best_ndm = ndms[best_ndm_index]
        
        
        if ben_only_flag:
            return_dict[str(i)]=[params, best_ndm.train.tot_time, best_ndm.soft_test.tot_time, best_ndm.soft_score, best_ndm]
        else:
            return_dict[str(i)]=[params, best_ndm.train.tot_time, best_ndm.test.tot_time, best_ndm.score, best_ndm]
            




            
    elif alg_type=='supervised':
        # create classification model
        print('Running supervised learning with model %s' % model_name)
        model, params = generate_model_sup(args,model_name)
        

        ndm = MODEL(model, score_metric='accuracy', verbose=10, random_state=seed)
        ndm.train(X_train,y_train)
     
        

    # evaluate the learned model
        if ben_only_flag:
            best_ndm.soft_test(X_test)
            return_dict[str(i)]=[params, best_ndm.train.tot_time, best_ndm.soft_test.tot_time, best_ndm.soft_score, best_ndm]
            history = best_ndm.history

    #         fpr, tpr, thresholds = ndm.history.roc_curve
        else:
            best_ndm.test(X_test, y_test)
            return_dict[str(i)]=[params, best_ndm.train.tot_time, best_ndm.test.tot_time, best_ndm.score, best_ndm]





    return best_ndm.history["score"], best_ndm.history["roc_curve"]


def main():
   
    rng = np.random.default_rng(seed)  # can be called without a seed

    parser = argparse.ArgumentParser()
    sample_rate = 1.0
    
    # Input args
    parser.add_argument('--data_rep',type=str,default='netml')
    parser.add_argument('--benign_sources',nargs='+')
    parser.add_argument('--mal_sources',nargs='+')
    parser.add_argument('--attack_types',nargs='+')
    parser.add_argument('--benign_folders',nargs='+')
    parser.add_argument('--mal_folders',nargs='+')
    
    # model arguments
    parser.add_argument('--num_agents', type =int, default = 1)
    parser.add_argument('--model_name', type =str, default = 'GMM')
    
    

    #### Van add this line so that we just have to decide whether it is supervised or unsupervised
    parser.add_argument('--training_type',type=str,default ='unsupervised')
    ################
    args = parser.parse_args()



    ben_only_flag=False
    assert args.benign_sources is not None
    if args.mal_sources is None:
        ben_only_flag=True
    
    training_type = args.training_type
    if training_type == "supervised":
        config = configparser.ConfigParser()
        config.read_file(open('src/netml/configs/default_parks.cfg'))
    else:
        config = configparser.ConfigParser()
        config.read_file(open('src/netml/configs/unsup_parks.cfg'))
        
    combined = config.getboolean('DATA','combined')
    distributed = config.getboolean('LEARNING','distributed')
    alg_type = config['LEARNING']['alg_type']

    if not combined:
        parser.add_argument('--train_sources',nargs='+',default=[])
        parser.add_argument('--test_sources',nargs='+',default=[])
 
    if distributed:
        # Federation args
        # imba for imbalanced split, seq_select to split data in order of appearance
        parser.add_argument('--imba', dest='imba', action='store_true')
        parser.add_argument('--seq_select', dest='seq_select', action='store_true')   
#     print(parser)

################## Van add this line of code


############# To change the level of sampling, change this line of code
    parser.add_argument('--sample_level', dest='sample_level',default= sample_rate)
    
##################
    

    args = parser.parse_args()


    data_source=config['DATA']['data_source'].split(',')
    benign_folders = args.benign_folders
    mal_folders = args.mal_folders
    

    if not combined:
        assert len(args.benign_sources)+len(args.mal_sources)==len(args.train_sources)+len(args.test_sources)


    print("it is good till here")

        
        

#     ################ When both of the training and testing are benign, we will pass the attack type to be "empty" #####
    
    if args.attack_types[0] == "empty":
        print("Loading data")
        print("this is testing of benign against benign")
        X_train, y_train, column_names = read_data_benign(args, config, "benign",benign_folders, mal_folders,args.data_rep, float(config['DATA']['train_test_split']),rng,alg_type,combined)
        y_train=np.zeros(len(y_train))
        X_test, y_test, column_names = read_data_benign(args, config, "malicious",benign_folders, mal_folders,args.data_rep, float(config['DATA']['train_test_split']),rng,alg_type,combined)
        y_test = np.zeros(len(y_test))
       
         
    else:
        # Load data
        print('Loading data') 
#        read_data(args, config, benign_folders, mal_folders, args.data_rep, float(config['DATA']['train_test_split']),rng,alg_type,combined)
        X_train, y_train, X_test, y_test, column_names = read_data(args, config, benign_folders, mal_folders, args.data_rep, float(config['DATA']['train_test_split']),rng,alg_type,combined)
        

        
    print("Load successfully")  
    
        ################# This is used for the case of benign versus benign #########
#     total_len = X_train.shape[0]
#     train_len = int(total_len*0.5)
#     train_indices = rng.choice(total_len,train_len,replace=False)
#     test_indices = np.setdiff1d(np.arange(total_len),train_indices) 


#     X_half_test = X_train[test_indices]
#     y_half_test = y_train[test_indices]
#     X_train = X_train[train_indices]
#     y_train = y_train[train_indices]
        
        
#         ############################ Van wrote this to see if sampling can helps to achieve the same level of performance###
        
    train_len= int(len(X_train)*sample_rate)
    train_indices=rng.choice(len(X_train),train_len,replace=False)


    X_train=X_train[train_indices]
    y_train=y_train[train_indices]

    print("train length")
    print(train_len)


        
#         ################################################################################################
        
        

    if args.num_agents>1:
        df_list=distribute_dataframe_np(X_train, y_train, args.num_agents, args.imba, args.seq_select, rng, label_name=column_names[-1])
    else:
        df_list=[(X_train,y_train)]
    
# #     # Run unsupervised learning
    manager = Manager()
    return_dict = manager.dict()

    
#     # Parallel run of all agents
# #     pool = multiprocessing.Pool() #use all available cores, otherwise specify the number you want as an argument
# #     for i, item in enumerate(df_list):
# #         pool.apply_async(model_run, args=(args, alg_type, data_source, seed, i, item[0], item[1], X_test, y_test, return_dict))
# #     pool.close()
# #     pool.join()


    for i, item in enumerate(df_list):
# #         print(return_dict)
        test_score, test_roc = model_run(args, alg_type, data_source, seed, i, item[0], item[1], X_test, y_test, ben_only_flag, return_dict)

    train_times=[]
    test_times=[]
    test_results=[]
    if alg_type=='supervised':
        ben_accs=[]
        mal_accs=[]
        overall_accs=[]
    model_details=[]
    num_agents=0
 #     print(return_dict)
    for k,v in return_dict.items():
        if num_agents==0:
            params=return_dict[k][0]
# #             print(params)
        num_agents+=1
# #         print(v)
        train_times.append(v[1])
        test_times.append(v[2])
        if not ben_only_flag:
            test_results.append(v[3])
        else:
            test_results.append(v[3])
        model_details.append(v[4])
        model = v[4]
        print(model.history)

        if alg_type=='supervised':
            ben_accs.append(model.history['ben_score'])
            mal_accs.append(model.history['mal_score'])
            overall_accs.append(model.history['score'])
   
    print('Number of working splits: %s' % num_agents)
   
    
    out_file_name=output_file_name(config,args)
    data_filename=out_file_name+'.txt'
    
    if ben_only_flag:
# #         return soft scores
# #         return_array=np.array(test_results)
        return_array=np.vstack((X_test[:,0],test_results))
        output_name='output/'
        for item in data_source:
            output_name+= item + '_'
        output_name+='test_scores_'
        output_name+=args.model_name
        output_name+='.npy'
        np.savetxt(output_name,return_array)
    else:
   
        if alg_type=='unsupervised':
            write_out(data_filename,config,args,params,train_times,test_times,test_results)
        elif alg_type=='supervised':
            write_out(data_filename,config,args,params,train_times,test_times,overall_accs,ben_accs,mal_accs)
    
    model_details_filename=out_file_name+'_ben_'
    for item in args.benign_sources:
        model_details_filename+=item
    if not ben_only_flag:
        model_details_filename+='_mal_'
        for item in args.mal_sources:
            model_details_filename+=item
    model_details_filename+='.pkl'
    
    
    dump_data(model_details,model_details_filename)
    print("good here")
   

if __name__ == '__main__':
    main()
