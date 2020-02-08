from Arithmos.classification import SklTreeLearner
from Arithmos.classification import TreeLearner as ClassificationTreeLearner
from Arithmos.modelling import Fitter, SklFitter
from Arithmos.regression import TreeLearner as RegressionTreeLearner
from Arithmos.regression.tree import SklTreeRegressionLearner
from Arithmos.tree import TreeModel

__all__ = ['SklTreeLearner', 'TreeLearner']


class SklTreeLearner(SklFitter):
    name = 'tree'

    __fits__ = {'classification': SklTreeLearner,
                'regression': SklTreeRegressionLearner}


class TreeLearner(Fitter):
    name = 'tree'

    __fits__ = {'classification': ClassificationTreeLearner,
                'regression': RegressionTreeLearner}

    __returns__ = TreeModel
