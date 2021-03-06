# Test methods with long descriptive names can omit docstrings
# pylint: disable=missing-docstring

import unittest
import inspect
import pkgutil
import traceback

import Arithmos
from Arithmos.data import Table, Variable
from Arithmos.regression import Learner
from Arithmos.tests import test_filename


class TestRegression(unittest.TestCase):
    def all_learners(self):
        regression_modules = pkgutil.walk_packages(
            path=Arithmos.regression.__path__,
            prefix="Arithmos.regression.",
            onerror=lambda x: None)
        for importer, modname, ispkg in regression_modules:
            try:
                module = pkgutil.importlib.import_module(modname)
            except ImportError:
                continue

            for name, class_ in inspect.getmembers(module, inspect.isclass):
                if issubclass(class_, Learner) and 'base' not in class_.__module__:
                    yield class_

    def test_adequacy_all_learners(self):
        for learner in self.all_learners():
            try:
                learner = learner()
                table = Table("iris")
                self.assertRaises(ValueError, learner, table)
            except TypeError as err:
                traceback.print_exc()
                continue

    def test_adequacy_all_learners_multiclass(self):
        for learner in self.all_learners():
            try:
                learner = learner()
                table = Table(test_filename("datasets/test8.tab"))
                self.assertRaises(ValueError, learner, table)
            except TypeError as err:
                traceback.print_exc()
                continue

    def test_missing_class(self):
        table = Table(test_filename("datasets/imports-85.tab"))
        for learner in self.all_learners():
            try:
                learner = learner()
                model = learner(table)
                model(table)
            except TypeError:
                traceback.print_exc()
                continue
