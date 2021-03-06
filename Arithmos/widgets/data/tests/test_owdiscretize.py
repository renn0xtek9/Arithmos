# Test methods with long descriptive names can omit docstrings
# pylint: disable=missing-docstring,unsubscriptable-object
from unittest.mock import Mock

from Arithmos.data import Table
from Arithmos.widgets.data.owdiscretize import OWDiscretize
from Arithmos.widgets.tests.base import WidgetTest
from arithmoswidget.widget import StateInfo


class TestOWDiscretize(WidgetTest):
    def setUp(self):
        self.widget = self.create_widget(OWDiscretize)

    def test_empty_data(self):
        """No crash on empty data"""
        data = Table("iris")
        widget = self.widget
        widget.default_method = 3
        self.send_signal(self.widget.Inputs.data,
                         Table.from_domain(data.domain))
        widget.unconditional_commit()

    def test_summary(self):
        """Check if status bar is updated when data is received"""
        input_sum = self.widget.info.set_input_summary = Mock()
        output_sum = self.widget.info.set_output_summary = Mock()

        data = Table("iris")
        self.send_signal(self.widget.Inputs.data, data)
        input_sum.assert_called_with(int(StateInfo.format_number(len(data))))
        output = self.get_output(self.widget.Outputs.data)
        output_sum.assert_called_with(int(StateInfo.format_number(len(output))))

        input_sum.reset_mock()
        output_sum.reset_mock()
        self.send_signal(self.widget.Inputs.data, None)
        input_sum.assert_called_once()
        self.assertEqual(input_sum.call_args[0][0].brief, "")
        output_sum.assert_called_once()
        self.assertEqual(output_sum.call_args[0][0].brief, "")
