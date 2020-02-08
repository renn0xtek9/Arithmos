import sklearn.neural_network as skl_nn
from Arithmos.base import NNBase
from Arithmos.regression import SklLearner
from Arithmos.classification.neural_network import NIterCallbackMixin

__all__ = ["NNRegressionLearner"]


class MLPRegressorWCallback(skl_nn.MLPRegressor, NIterCallbackMixin):
    pass


class NNRegressionLearner(NNBase, SklLearner):
    __wraps__ = MLPRegressorWCallback

    def _initialize_wrapped(self):
        clf = SklLearner._initialize_wrapped(self)
        clf.arithmos_callback = getattr(self, "callback", None)
        return clf
