from Arithmos.widgets import widget, gui
from Arithmos.widgets.settings import Setting

class OWWidgetName(widget.OWWidget):
    name = "Widget Name"
    id = "arithmos.widgets.widget_category.widget_name"
    description = ""
    icon = "icons/Unknown.svg"
    priority = 10
    category = ""
    keywords = ["list", "of", "keywords"]
    outputs = [("Name", type)]
    inputs = [("Name", type, "handler")]

    want_main_area = False

    foo = Setting(True)

    def __init__(self):
        super().__init__()

        # controls
        gui.rubber(self.controlArea)

    def handler(self, obj):
        pass
