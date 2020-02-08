import copy

import numpy as np

from Arithmos.data import Table
import Arithmos.evaluation
import Arithmos.classification

from Arithmos.widgets.evaluate.tests.base import EvaluateTest
from Arithmos.widgets.tests.base import WidgetTest
from Arithmos.widgets.tests.utils import simulate
from Arithmos.widgets.evaluate.owliftcurve import OWLiftCurve
from Arithmos.tests import test_filename

class TestOWLiftCurve(WidgetTest, EvaluateTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.lenses = data = Table(test_filename("datasets/lenses.tab"))
        cls.res = Arithmos.evaluation.TestOnTestData(
            train_data=data[::2], test_data=data[1::2],
            learners=[Arithmos.classification.MajorityLearner(),
                      Arithmos.classification.KNNLearner()],
            store_data=True,
        )

    def setUp(self):
        super().setUp()
        self.widget = self.create_widget(
            OWLiftCurve,
            stored_settings={
                "display_convex_hull": True
            }
        )  # type: OWLiftCurve

    def test_basic(self):
        self.send_signal(self.widget.Inputs.evaluation_results, self.res)
        simulate.combobox_run_through_all(self.widget.target_cb)

    def test_empty_input(self):
        res = copy.copy(self.res)
        res.actual = res.actual[:0]
        res.row_indices = res.row_indices[:0]
        res.predicted = res.predicted[:, :0]
        res.probabilities = res.probabilities[:, :0, :]
        self.send_signal(self.widget.Inputs.evaluation_results, res)

    def test_nan_input(self):
        res = copy.copy(self.res)
        res.actual[0] = np.nan
        self.send_signal(self.widget.Inputs.evaluation_results, res)
        self.assertTrue(self.widget.Error.invalid_results.is_shown())
        self.send_signal(self.widget.Inputs.evaluation_results, None)
        self.assertFalse(self.widget.Error.invalid_results.is_shown())
