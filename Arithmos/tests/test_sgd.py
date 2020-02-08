# Test methods with long descriptive names can omit docstrings
# pylint: disable=missing-docstring

import unittest
import warnings

import numpy as np
from sklearn.exceptions import ConvergenceWarning

from Arithmos.data import Table
from Arithmos.classification import SGDClassificationLearner
from Arithmos.regression import SGDRegressionLearner
from Arithmos.evaluation import CrossValidation, RMSE, AUC


class TestSGDRegressionLearner(unittest.TestCase):
    def setUp(self):
        # Convergence warnings are irrelevant for these tests
        warnings.filterwarnings("ignore", ".*", ConvergenceWarning)
        super().setUp()

    def test_SGDRegression(self):
        nrows, ncols = 500, 5
        X = np.random.rand(nrows, ncols)
        y = X.dot(np.random.rand(ncols))
        data = Table.from_numpy(None, X, y)
        sgd = SGDRegressionLearner()
        cv = CrossValidation(k=3)
        res = cv(data, [sgd])
        self.assertLess(RMSE(res)[0], 0.1)

    def test_coefficients(self):
        lrn = SGDRegressionLearner()
        mod = lrn(Table("housing"))
        self.assertEqual(len(mod.coefficients), len(mod.domain.attributes))


class TestSGDClassificationLearner(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.iris = Table('iris')

    def setUp(self):
        # Convergence warnings are irrelevant for these tests
        warnings.filterwarnings("ignore", ".*", ConvergenceWarning)
        super().setUp()

    def test_SGDClassification(self):
        sgd = SGDClassificationLearner()
        cv = CrossValidation(k=3)
        res = cv(self.iris, [sgd])
        self.assertGreater(AUC(res)[0], 0.8)

    def test_coefficients(self):
        lrn = SGDClassificationLearner()
        mod = lrn(self.iris)
        self.assertEqual(len(mod.coefficients[0]), len(mod.domain.attributes))
