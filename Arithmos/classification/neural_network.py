import sklearn.neural_network as skl_nn
from Arithmos.base import NNBase
from Arithmos.classification import SklLearner

__all__ = ["NNClassificationLearner"]


class NIterCallbackMixin:
    arithmos_callback = None

    @property
    def n_iter_(self):
        return self.__arithmos_n_iter

    @n_iter_.setter
    def n_iter_(self, v):
        self.__arithmos_n_iter = v
        if self.arithmos_callback:
            self.arithmos_callback(v)


class MLPClassifierWCallback(skl_nn.MLPClassifier, NIterCallbackMixin):
    pass


class NNClassificationLearner(NNBase, SklLearner):
    __wraps__ = MLPClassifierWCallback

    def _initialize_wrapped(self):
        clf = SklLearner._initialize_wrapped(self)
        clf.arithmos_callback = getattr(self, "callback", None)
        return clf
