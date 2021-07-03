# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 15:16:32 2021

@author: romain
"""
import numpy as np

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.base import BaseEstimator, TransformerMixin
# =============================================================================
# 
# =============================================================================
class MyStandardScaler(BaseEstimator, TransformerMixin):
    def __init__(self, with_mean=True):
        """
        Parameters
        ----------
        with_mean : Bool
            Use mean to center data. The default is True.
            If False only std is computed and used.

        Returns
        -------
        None.

        """
        self.with_mean = with_mean
    
    def fit(self, X, y=None):
        if self.with_mean:
            self.mean_ = X.mean(axis=0)
        self.std_ = X.std(axis=0)
        return self
    
    def transform(self, X):
        # if self.with_mean:
        #     return (X-self.mean_)/self.std_
        # return X/self.std_
        return (X-self.mean_)/self.std_ if self.with_mean else X/self.std_
# =============================================================================
# 
# =============================================================================
if __name__=='__main__':
    X, y = load_iris('data')
    
    scaler = MyStandardScaler(with_mean=False)
    # scaler.fit(X)
    # X_scaled = scaler.transform(X)
    
    X_scaled = scaler.fit_transform(X)
    print(scaler.get_params())








