from AnyQt.QtCore import  Qt
from AnyQt.QtGui import QColor

from Arithmos.widgets.tests.base import WidgetTest
from Arithmos.widgets.utils.colorpalette import ColorPaletteDlg


class TestColorPalette(WidgetTest):
    def test_colorpalette(self):
        dlg = ColorPaletteDlg(None)

        dlg.createContinuousPalette(
            "", "Gradient palette", False, QColor(Qt.white), QColor(Qt.black))

        dlg.contLeft.getColor().getRgb()
        dlg.contRight.getColor().getRgb()
        dlg.contpassThroughBlack
