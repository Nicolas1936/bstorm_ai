import numpy as np
from sklearn.datasets import load_iris

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder

from sklearn.base import BaseEstimator, TransformerMixin
#BaseEstimator : ajouts les getters et les setters
#TransformerMixin : ajout une methode fit_transform (!!! ne pas oublier retrun self à fit!!!)

class MyStandardScaler(BaseEstimator, TransformerMixin):
    def __init__(self, with_mean=True):
        """
        Parameters:
        -----------
            with_mean : bool 
                Use mean to center data. Defaults to True.
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
        if self.with_mean:
            return (X - self.mean_) / self.std_
        return X / self.std_

    #def fit_transform(self, X, y=None):
    #    return self.fit(X).transform(X)


if __name__ == '__main__':
    X, y = load_iris('data')
    scaler = MyStandardScaler(with_mean=False)
    #scaler.fit(X)
    #X_scaled = scaler.transform(X)
    #print(X_scaled)

    X_scaled2 = scaler.fit_transform(X)
    print(X_scaled2)

    print(scaler.get_params())