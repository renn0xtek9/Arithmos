from Arithmos.base import RandomForestModel
from Arithmos.classification import RandomForestLearner as RFClassification
from Arithmos.data import Variable
from Arithmos.modelling import SklFitter
from Arithmos.preprocess.score import LearnerScorer
from Arithmos.regression import RandomForestRegressionLearner as RFRegression

__all__ = ['RandomForestLearner']


class _FeatureScorerMixin(LearnerScorer):
    feature_type = Variable
    class_type = Variable

    def score(self, data):
        model = self.get_learner(data)(data)
        return model.skl_model.feature_importances_, model.domain.attributes


class RandomForestLearner(SklFitter, _FeatureScorerMixin):
    name = 'random forest'

    __fits__ = {'classification': RFClassification,
                'regression': RFRegression}

    __returns__ = RandomForestModel
