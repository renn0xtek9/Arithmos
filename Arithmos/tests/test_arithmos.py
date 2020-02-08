import unittest


class TestArithmos(unittest.TestCase):
    def test_arithmos_has_modules(self):
        import pkgutil
        import Arithmos
        unimported = ['canvas', 'datasets', 'testing', 'tests', 'setup',
                      'util', 'widgets']
        for _, name, __ in pkgutil.iter_modules(Arithmos.__path__):
            if name not in unimported:
                self.assertIn(name, Arithmos.__dict__)
