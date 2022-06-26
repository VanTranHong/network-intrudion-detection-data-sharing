"""RF

"""
# Authors: kun.bj@outlook.com
#
# License: xxx

from sklearn.ensemble import RandomForestClassifier
import numpy as np


class RF(RandomForestClassifier):

    def __init__(self, n_estimators=100, *, criterion='gini', max_depth=None, min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features='auto', max_leaf_nodes=None, min_impurity_decrease=0.0, min_impurity_split=None, bootstrap=True, oob_score=False, n_jobs=None, random_state=None, verbose=0, warm_start=False, class_weight=None, ccp_alpha=0.0, max_samples=None):
        super(RF, self).__init__(
n_estimators, criterion, max_depth, min_samples_split, min_samples_leaf, min_weight_fraction_leaf, max_features, max_leaf_nodes, min_impurity_decrease, min_impurity_split, bootstrap, oob_score, n_jobs, random_state, verbose, warm_start, class_weight, ccp_alpha, max_samples)

        self.random_state = random_state
        self.verbose = verbose

        
    def predict_func(self,X):
        return np.argmax(self.predict_proba(X), axis=1)
