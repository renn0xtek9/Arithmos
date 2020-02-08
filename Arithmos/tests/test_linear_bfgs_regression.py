# Test methods with long descriptive names can omit docstrings
# pylint: disable=missing-docstring

import unittest

from Arithmos.data import Table
from Arithmos.evaluation import CrossValidation, RMSE
from Arithmos.regression.linear_bfgs import LinearRegressionLearner


class TestLinearRegressionLearner(unittest.TestCase):
    def test_preprocessors(self):
        table = Table('housing')
        learners = [LinearRegressionLearner(preprocessors=[]),
                    LinearRegressionLearner()]
        cv = CrossValidation(k=3)
        results = cv(table, learners)
        rmse = RMSE(results)
        self.assertLess(rmse[0], rmse[1])
