"""Detection model
    train and test a model on a given data
"""
# Authors: kun.bj@outlook.com
#
# License: xxx

from sklearn import metrics
from sklearn.metrics import roc_curve

import numpy as np

from ...netml.utils.tool import timing
import math


class MODEL:
    def __init__(self, model=None, *, score_metric='auc', verbose=1, random_state=42):
        """Train and test a model on a given data.

        Parameters
        ----------
        model: instance
            a detection model instance.

        score_metric: str (default is 'auc')
            a score we used to evaluate the model

        verbose: int (default is 1)
            a print level is to control what information should be printed according to the given value.
            The higher the value is, the more info is printed.

        random_state: int
            a value is to make your experiments more reproducible.

        Returns
        -------
            a MODEL instance
        """

        self.model = model
        self.model_name = model.name
        self.score_metric = score_metric
        self.verbose = verbose
        self.random_state = random_state
        # store all data generated during training and testing the model.
        self.history = {}

    @timing
    def _train(self, X_train, y_train=None):
        """fit the model on the train set

        Parameters
        ----------
        X_trian: array

        y_train: array (default is None)
            in unsupervised learning setting, there is no requirement of ground truth to fit the model

        Returns
        -------
            self
        """

        self.model.fit(X_train, y_train)

    def train(self, X_train, y_train=None):
        """fit the model on the train set

        Parameters
        ----------
        X_trian: array

        y_train: array (default is None)
            in unsupervised learning setting, there is no requirement of ground truth to fit the model

        Returns
        -------
            self
        """
        _, tot_time = self._train(X_train, y_train)
        self.train.__dict__['tot_time'] = tot_time

    @timing
    def _test(self, X_test, y_test):
        """Evaluate the model on the test set

        Parameters
        ----------
        X_test: array

        y_test: array
            ground true

        Returns
        -------
            self
        """

        if self.score_metric == 'auc':
            y_score = self.model.decision_function(X_test)

            # For binary  y_true, y_score is supposed to be the score of the class with greater label.
            # pos_label = 1, so y_score should be the corresponding score (i.e., novel score)
            self.fpr, self.tpr, self.thresholds = roc_curve(y_test, y_score, pos_label=1)
            print("False positive rate")
            print(self.fpr)
            print(" True positive rate")
            print(self.tpr)
            print(self.thresholds)
            print(" Type of TPR")
#             print(type(self.tpr))

            if math.isnan(self.tpr[0]) == False:
                self.score = metrics.auc(self.fpr, self.tpr)
            else:
                #### when auc is not available, we use accuracy instead
#                 y_hat = self.model.predict_func(X_test)
                self.score = 0
               
            self.history['score'] = y_score
            
            self.history['roc_curve'] = [self.fpr, self.tpr, self.thresholds]
            self.history['predictions'] = y_score
#             self.history['fpr'] = self.fpr
#             self.history['thresholds'] = self.thresholds
            
        elif self.score_metric == 'accuracy':
            # Directly using predict function for supervised classification
            y_hat = self.model.predict_func(X_test)
            self.score = metrics.accuracy_score(y_test,y_hat)
            
            mal_indices=np.where(y_test!=0)
            benign_indices=np.where(y_test==0)
            
            y_hat_mal = self.model.predict_func(X_test[mal_indices])
            y_hat_ben = self.model.predict_func(X_test[benign_indices])
            
            self.mal_score = metrics.accuracy_score(y_test[mal_indices],y_hat_mal)
            self.ben_score = metrics.accuracy_score(y_test[benign_indices],y_hat_ben)
            
            self.history['score'] = self.score
            self.history['mal_score'] = self.mal_score
            self.history['ben_score'] = self.ben_score
            self.history['predictions'] = y_hat
            

    def test(self, X_test, y_test):
        """Evaluate the model on the test set

        Parameters
        ----------
        X_test: array

        y_test: array
            ground true

        Returns
        -------
            self
        """
        _, tot_time = self._test(X_test, y_test)
        self.test.__dict__['tot_time'] = tot_time
        
    @timing
    def _soft_test(self, X_test):
        """Evaluate the model on the test set

        Parameters
        ----------
        X_test: array

        Returns
        -------
            self
        """
        self.soft_score = self.model.decision_function(X_test)
        self.history['predictions'] = self.soft_score
        
        
        
    def soft_test(self, X_test):
        """Get scores on the test set

        Parameters
        ----------
        X_test: array

        Returns
        -------
            self
        """
        
        
        _, tot_time = self._soft_test(X_test)
        self.soft_test.__dict__['tot_time'] = tot_time
