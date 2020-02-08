from Arithmos.classification import MajorityLearner
from Arithmos.modelling import Fitter
from Arithmos.regression import MeanLearner

__all__ = ['ConstantLearner']


class ConstantLearner(Fitter):
    __fits__ = {'classification': MajorityLearner, 'regression': MeanLearner}
