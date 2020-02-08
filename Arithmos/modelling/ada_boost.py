from Arithmos.base import SklModel
from Arithmos.ensembles import (
    SklAdaBoostClassificationLearner, SklAdaBoostRegressionLearner
)
from Arithmos.modelling import SklFitter

__all__ = ['SklAdaBoostLearner']


class SklAdaBoostLearner(SklFitter):
    __fits__ = {'classification': SklAdaBoostClassificationLearner,
                'regression': SklAdaBoostRegressionLearner}

    __returns__ = SklModel
