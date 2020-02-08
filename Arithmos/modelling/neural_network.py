from Arithmos.classification import NNClassificationLearner
from Arithmos.modelling import SklFitter
from Arithmos.regression import NNRegressionLearner

__all__ = ['NNLearner']


class NNLearner(SklFitter):
    __fits__ = {'classification': NNClassificationLearner,
                'regression': NNRegressionLearner}

    callback = None

    def get_learner(self, problem_type):
        learner = super().get_learner(problem_type)
        learner.callback = self.callback
        return learner
