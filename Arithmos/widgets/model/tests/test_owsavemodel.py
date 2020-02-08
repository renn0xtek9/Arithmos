import unittest

from Arithmos.classification.majority import MajorityLearner
from Arithmos.data import Table
from Arithmos.widgets.model.owsavemodel import OWSaveModel
from Arithmos.widgets.utils.save.tests.test_owsavebase import \
    SaveWidgetsTestBaseMixin
from Arithmos.widgets.tests.base import WidgetTest


class OWSaveTestBase(WidgetTest, SaveWidgetsTestBaseMixin):
    def setUp(self):
        self.widget = self.create_widget(OWSaveModel)
        self.model = MajorityLearner(Table("iris"))


if __name__ == "__main__":
    unittest.main()
