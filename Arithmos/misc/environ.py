"""
Retrive basic library/application data/cache locations.

The basic FS layout for Arithmos data files is

$DATA_HOME/Arithmos/$VERSION/
    widgets/
    canvas/

where DATA_HOME is a platform dependent application directory
(:ref:`data_dir_base`) and VERSION is Arithmos.__version__ string.
"""
import os
import sys
import warnings

import Arithmos


def data_dir_base():
    """
    Return the platform dependent application directory.

    This is usually

        - on windows: "%USERPROFILE%\\AppData\\Local\\"
        - on OSX:  "~/Library/Application Support/"
        - other: "~/.local/share/
    """

    if sys.platform == "darwin":
        base = os.path.expanduser("~/Library/Application Support")
    elif sys.platform == "win32":
        base = os.getenv("APPDATA", os.path.expanduser("~/AppData/Local"))
    elif os.name == "posix":
        base = os.getenv('XDG_DATA_HOME', os.path.expanduser("~/.local/share"))
    else:
        base = os.path.expanduser("~/.local/share")
    return base


def data_dir(versioned=True):
    """
    Return the platform dependent Arithmos data directory.

    This is ``data_dir_base()``/Arithmos/__VERSION__/ directory if versioned is
    `True` and ``data_dir_base()``/Arithmos/ otherwise.
    """
    base = data_dir_base()
    if versioned:
        return os.path.join(base, "Arithmos", Arithmos.__version__)
    else:
        return os.path.join(base, "Arithmos")


def widget_settings_dir(versioned=True):
    """
    Return the platform dependent directory where widgets save their settings.

    .. deprecated:: 3.23
    """
    warnings.warn(
        f"'{__name__}.widget_settings_dir' is deprecated.",
        DeprecationWarning, stacklevel=2
    )
    import arithmoswidget.settings
    return arithmoswidget.settings.widget_settings_dir(versioned)


def cache_dir(*args):
    """
    Return the platform dependent Arithmos cache directory.
    """
    if sys.platform == "darwin":
        base = os.path.expanduser("~/Library/Caches")
    elif sys.platform == "win32":
        base = os.getenv("APPDATA", os.path.expanduser("~/AppData/Local"))
    elif os.name == "posix":
        base = os.getenv("XDG_CACHE_HOME", os.path.expanduser("~/.cache"))
    else:
        base = os.path.expanduser("~/.cache")

    base = os.path.join(base, "Arithmos", Arithmos.__version__)
    if sys.platform == "win32":
        # On Windows cache and data dir are the same.
        # Microsoft suggest using a Cache subdirectory
        return os.path.join(base, "Cache")
    else:
        return base
