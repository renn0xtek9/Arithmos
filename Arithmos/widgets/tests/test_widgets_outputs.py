import itertools
import re
import unittest
import importlib.util

from arithmoscanvas.registry import WidgetRegistry
from Arithmos.canvas.config import Config


class TestWidgetOutputs(unittest.TestCase):
    def test_outputs(self):
        re_send = re.compile('\\n\s+self.send\("([^"]*)"')
        disc = Config.widget_discovery(WidgetRegistry())
        disc.run(itertools.islice(Config.widgets_entry_points(), 0, 1))
        errors = []
        for desc in disc.registry.widgets():
            signal_names = {output.name for output in desc.outputs}
            module_name, class_name = desc.qualified_name.rsplit(".", 1)
            fname = importlib.util.find_spec(module_name).origin
            with open(fname, encoding='utf-8') as f:
                widget_code = f.read()
            used = set(re_send.findall(widget_code))
            undeclared = used - signal_names
            if undeclared:
                errors.append("- {} ({})".
                              format(desc.name, ", ".join(undeclared)))
        if errors:
            self.fail("Some widgets send to undeclared outputs:\n"+"\n".
                      join(errors))
