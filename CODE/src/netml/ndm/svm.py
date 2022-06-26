"""SVM

"""
# Authors: kun.bj@outlook.com
#
# License: xxx

from sklearn.linear_model import SGDClassifier
import numpy as np


class SVM(SGDClassifier):

    def __init__(self, loss='hinge', *, penalty='l2', alpha=0.0001, l1_ratio=0.15, fit_intercept=True, max_iter=1000, tol=0.001, shuffle=True, verbose=0, epsilon=0.1, n_jobs=None, random_state=None, learning_rate='optimal', eta0=0.0, power_t=0.5, early_stopping=False, validation_fraction=0.1, n_iter_no_change=5, class_weight=None, warm_start=False, average=False):
        super(SVM, self).__init__(
loss, penalty, alpha, l1_ratio, fit_intercept, max_iter, tol, shuffle, verbose, epsilon, n_jobs, random_state, learning_rate, eta0, power_t, early_stopping, validation_fraction, n_iter_no_change, class_weight, warm_start, average)

        self.random_state = random_state
        self.verbose = verbose
        
    def predict_func(self,X):
        y_score = self.decision_function(X)
        y_hat = np.sign(y_score)
        y_hat[np.where(y_hat==-1)]=0
        return y_hat

    def predict_proba(self, X):
        raise NotImplementedError
