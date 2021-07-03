# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 13:56:39 2021

@author: romain
"""
import numpy as np
from time import perf_counter as pc

from decision_tree_classifier import MyDecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
# =============================================================================
# 
# =============================================================================
class MyRandomForestClassifier():
    def __init__(self, n_estimators=100, max_samples=.8, criterion='gini', max_depth=None):
        self.n_estimators = n_estimators
        self.max_samples = max_samples
        self.criterion = criterion
        self.max_depth = max_depth
    
    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.trees_ = []
        for i in range(self.n_estimators):
            model = MyDecisionTreeClassifier(self.criterion, self.max_depth)
            idx = self._get_idx(self.max_samples, n_samples)
            X_resampled, y_resampled = X[idx,:], y[idx]
            model.fit(X_resampled, y_resampled)
            self.trees_.append(model)
        return self
    
    def predict(self, X):
        n_samples, _ = X.shape
        y_pred = np.empty(n_samples, dtype=np.int32)
        for i in range(n_samples):
            y_pred[i] = self._aggregate(X[i,:].reshape(1,4))
        return y_pred
    
    def _aggregate(self, X):
        y_pred = np.empty(len(self.trees_))
        for i, tree in enumerate(self.trees_):
            y_pred[i] = tree.predict(X)[0]
        class_, counts = np.unique(y_pred, return_counts=True)
        return class_[np.argmax(counts)].astype(int)

    def _get_idx(self, max_samples, n_samples):
        return np.random.choice(n_samples, int(n_samples*max_samples), replace=False)
    
    def score(self, X, y):
        y_pred = self.predict(X)
        return ((y_pred == y).sum()/y.shape)[0]
# =============================================================================
# 
# =============================================================================
if __name__=='__main__':
    np.random.seed(1)
    data = load_iris(as_frame=True)['frame']
    X = data.drop(columns='target').values
    y = data['target'].values
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.60)
    
    model = MyRandomForestClassifier(100, max_samples=0.6)
    model_sk = RandomForestClassifier(100, max_samples=0.6)
    
    model.fit(X_train, y_train)
    model_sk.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    print(model.score(X_test, y_test))
    print(model_sk.score(X_test, y_test))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    