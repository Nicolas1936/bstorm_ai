#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 13:54:55 2021

@author: blanchardnicolas
"""

import numpy as np

#a = np.array([1, 2, 3])
#print(np.random.choice(10000, 500, replace=True))
#print(np.random.choice(a, 2, replace=False))

from decision_tree_classifier import MyDecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.base import BaseEstimator

class MyRandomForestClassifier(BaseEstimator):
    def __init__(self, n_estimators=2, max_depth=None):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        
        self.model = MyDecisionTreeClassifier()
    
    def fit(self, X, y):
        self._encoder = LabelEncoder()
        y = self._encoder.fit_transform(y)
        
        tree_pred = np.empty(self.n_estimators, dtype=np.int64)
        for i in range(self.n_estimators):
            #tree_pred[i] = self.model.fit(X, y)
            pass
    
    def predict(self, X):
        pass


if __name__ == '__main__':
    np.random.seed(1)
    data = load_iris(as_frame=True)['frame']
    X = data.drop(columns='target').values
    y = data['target'].values
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.20)
    
    max_samples = 0.7
    print(int(X_train.shape[0]*max_samples))
    
    
    model = MyRandomForestClassifier()
    
    #
    
    #model.fit(X, y)
    
    #test = np.random.choice(X, 2, replace=False)
    