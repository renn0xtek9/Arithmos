import sklearn.neighbors as skl_neighbors
from Arithmos.base import KNNBase
from Arithmos.classification import SklLearner

__all__ = ["KNNLearner"]


class KNNLearner(KNNBase, SklLearner):
    __wraps__ = skl_neighbors.KNeighborsClassifier
