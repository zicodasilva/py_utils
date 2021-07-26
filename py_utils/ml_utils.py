"""
Useful abractions when working with machine learning algorithms.

@author: Zico da Silva
"""
import numpy as np
from sklearn.linear_model import LinearRegression

class LinearPredictionModel(LinearRegression):
    """
    This model is for prediction only.  It has no fit method.
    You can initialize it with fixed values for coefficients
    and intercepts.

    Parameters
    ----------
    coef, intercept : arrays
        See attribute descriptions below.

    Attributes
    ----------
    coef_ : array of shape (n_features, ) or (n_targets, n_features)
        Coefficients of the linear model.  If there are multiple targets
        (y 2D), this is a 2D array of shape (n_targets, n_features),
        whereas if there is only one target, this is a 1D array of
        length n_features.
    intercept_ : float or array of shape of (n_targets,)
        Independent term in the linear model.
    """

    def __init__(self, coef=None, intercept=None):
        if coef is not None:
            coef = np.array(coef)
            if intercept is None:
                intercept = np.zeros(coef.shape[0])
            else:
                intercept = np.array(intercept)
            assert coef.shape[0] == intercept.shape[0]
        else:
            if intercept is not None:
                raise ValueError("Provide coef only or both coef and intercept")
        self.intercept_ = intercept
        self.coef_ = coef

    def fit(self, X, y):
        """This model does not have a fit method."""
        raise NotImplementedError("model is only for prediction")
