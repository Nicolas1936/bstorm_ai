# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 14:20:24 2021

@author: romain
"""
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.base import BaseEstimator
# =============================================================================
# 
# =============================================================================
class MyDecisionTreeClassifier(BaseEstimator):
    def __init__(self, criterion='gini', max_depth=None):
        self.criterion = criterion
        self.max_depth = max_depth
    
    def fit(self, X, y):
        self._encoder = LabelEncoder()
        y = self._encoder.fit_transform(y)
        self.tree_ = self._get_split(X, y, depth=0)
        return self
    
    def predict(self, X):
        n_samples, n_features = X.shape
        y_pred = np.empty(n_samples, dtype=np.int64)
        for i in range(n_samples):
            y_pred[i] = self._get_prediction(X[i,:].reshape(1, n_features), self.tree_)
        y_pred = self._encoder.inverse_transform(y_pred)
        return y_pred
    
    def _get_split(self, X, y, depth=0):
        best_gini = 1000
        
        # criterion
        for i in range(X.shape[1]):
            for condition in np.unique(X[:,i]):
                left, right = y[X[:,i] <= condition], y[X[:,i] > condition]
                gini = self._get_gini((left, right), X.shape[0])
                if gini < best_gini:
                    best_gini = gini
                    best_feature = i
                    best_condition = condition
        
        depth += 1
        
        node={'condition':best_condition,
              'feature':best_feature,
              'gini':best_gini,
              'left':(X[X[:,best_feature] <= best_condition], y[X[:,best_feature] <= best_condition]),
              'right':(X[X[:,best_feature] > best_condition], y[X[:,best_feature] > best_condition]),
              'depth':depth}   
    
        for side in ['left','right']:
            if len(np.unique(node[side][1])) == 1:
                node[side] = np.unique(node[side][1])[0]
            elif len(np.unique(left[1])) == 0:
                node[side] = None
            else:
                if self.max_depth == depth:
                    node[side] = self._get_leaf(node[side][1])
                else:
                    node[side] = self._get_split(node[side][0], node[side][1], depth=depth)
        return node
    
    def _get_gini(self, groups, n_samples):
        gini = 0
        for gr in groups:
            _, p = np.unique(gr, return_counts=True)
            p = p/gr.shape[0]
            gini += (1-(p*p).sum())*(gr.shape[0]/n_samples)
        return gini 
    
    def _get_leaf(self, y):
        class_, count = np.unique(y, return_counts=True)
        class_ = class_[count==np.max(count)]
        return np.random.choice(class_)

    def _get_prediction(self, X, tree): 
        if X[0,tree['feature']] <= tree['condition']:
            if isinstance(tree['left'], np.int64):
                return tree['left']
            elif isinstance(tree['left'], dict):
                return self._get_prediction(X, tree['left'])
            else:
                return self._get_prediction(X, tree['right'])
            
        else:
            if isinstance(tree['right'], np.int64):
                return tree['right']
            elif isinstance(tree['right'], dict):
                return self._get_prediction(X, tree['right'])
            else:
                return self._get_prediction(X, tree['left'])
    
    def score(self, X, y):
        y_pred = self.predict(X)
        good_pred = y_pred == y
        good_pred = good_pred.sum()
        good_pred = good_pred/y_pred.shape
        return good_pred[0]
        # return (y_pred == y).sum()/y.shape
         
# =============================================================================
# 
# =============================================================================
if __name__=='__main__':
    np.random.seed(1)
    data = load_iris(as_frame=True)['frame']
    X = data.drop(columns='target').values
    y = data['target'].values
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.40)
    
    model = MyDecisionTreeClassifier()
    sk_model = DecisionTreeClassifier()
    
    model.fit(X_train, y_train)
    sk_model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
   
    results = pd.DataFrame({'y_true':y_test,'y_pred':y_pred})
    
    print(model.score(X_test, y_test))
    print(sk_model.score(X_test, y_test))









