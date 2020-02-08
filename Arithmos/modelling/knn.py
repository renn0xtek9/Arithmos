from Arithmos.classification import KNNLearner as KNNClassification
from Arithmos.modelling import SklFitter
from Arithmos.regression import KNNRegressionLearner

__all__ = ['KNNLearner']


class KNNLearner(SklFitter):
    __fits__ = {'classification': KNNClassification,
                'regression': KNNRegressionLearner}
