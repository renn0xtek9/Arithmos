from os.path import dirname
import unittest

import Arithmos


def suite(loader=None, pattern='test*.py'):
    top_level_dir = dirname(dirname(Arithmos.__file__))
    return unittest.TestSuite(loader.discover(dirname(__file__),
                                              pattern or 'test*.py',
                                              top_level_dir))


def load_tests(loader, tests, pattern):
    return suite(loader, pattern)


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
