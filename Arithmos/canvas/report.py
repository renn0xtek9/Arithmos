import sys
import warnings
import Arithmos.widgets.report

warnings.warn(
    f"'{__name__}' is deprecated and will be removed in the future.\n"
    "The contents of this package were moved to 'Arithmos.widgets.report'. "
    "Please update the imports accordingly.",
    FutureWarning, stacklevel=2
)
sys.modules[__name__] = Arithmos.widgets.report
