import sklearn.neighbors as skl_neighbors
from Arithmos.base import KNNBase
from Arithmos.regression import SklLearner

__all__ = ["KNNRegressionLearner"]


class KNNRegressionLearner(KNNBase, SklLearner):
    __wraps__ = skl_neighbors.KNeighborsRegressor
