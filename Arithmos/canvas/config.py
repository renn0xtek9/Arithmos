"""
Arithmos Canvas Configuration

"""
import uuid
import warnings

import os
import sys
import itertools
from distutils.version import LooseVersion

from typing import Dict, Any, Optional, Iterable, List

import pkg_resources
import requests

from AnyQt.QtGui import QPainter, QFont, QFontMetrics, QColor, QPixmap, QIcon
from AnyQt.QtCore import Qt, QPoint, QRect

from arithmoscanvas import config as occonfig
from arithmoscanvas.utils.settings import config_slot
from arithmoswidget.workflow import config

import Arithmos

# generated from biolab/arithmos-addons repository
OFFICIAL_ADDON_LIST = "https://arithmos.biolab.si/addons/list"

WIDGETS_ENTRY = "arithmos.widgets"

spec = [
    ("startup/check-updates", bool, False, "Check for updates"),

    ("startup/launch-count", int, 0, ""),

    ("reporting/machine-id", str, str(uuid.uuid4()), ""),

    ("reporting/send-statistics", bool, False, ""),

    ("reporting/permission-requested", bool, False, ""),

    ("notifications/check-notifications", bool, True, "Check for notifications"),

    ("notifications/announcements", bool, True,
     "Show notifications about Biolab announcements"),

    ("notifications/blog", bool, True,
     "Show notifications about blog posts"),

    ("notifications/new-features", bool, True,
     "Show notifications about new features"),

    ("notifications/displayed", str, 'set()',
     "Serialized set of notification IDs which have already been displayed")
]

spec = [config_slot(*t) for t in spec]


class Config(config.Config):
    """
    Arithmos application configuration
    """
    OrganizationDomain = "biolab.si"
    ApplicationName = "Arithmos"
    ApplicationVersion = Arithmos.__version__

    def init(self):
        super().init()
        for t in spec:
            occonfig.register_setting(*t)

    @staticmethod
    def application_icon():
        """
        Return the main application icon.
        """
        path = pkg_resources.resource_filename(
            __name__, "icons/arithmos-canvas.svg"
        )
        return QIcon(path)

    @staticmethod
    def splash_screen():
        path = pkg_resources.resource_filename(
            __name__, "icons/arithmos-splash-screen.png")
        pm = QPixmap(path)

        version = Config.ApplicationVersion
        if version:
            version_parsed = LooseVersion(version)
            version_comp = version_parsed.version
            version = ".".join(map(str, version_comp[:2]))
        size = 21 if len(version) < 5 else 16
        font = QFont("Helvetica")
        font.setPixelSize(size)
        font.setBold(True)
        font.setItalic(True)
        font.setLetterSpacing(QFont.AbsoluteSpacing, 2)
        metrics = QFontMetrics(font)
        br = metrics.boundingRect(version).adjusted(-5, 0, 5, 0)
        br.moveCenter(QPoint(436, 224))

        p = QPainter(pm)
        p.setRenderHint(QPainter.Antialiasing)
        p.setRenderHint(QPainter.TextAntialiasing)
        p.setFont(font)
        p.setPen(QColor("#231F20"))
        p.drawText(br, Qt.AlignCenter, version)
        p.end()
        return pm, QRect(88, 193, 200, 20)

    @staticmethod
    def widgets_entry_points():
        """
        Return an `EntryPoint` iterator for all 'arithmos.widget' entry
        points.
        """
        # Ensure the 'this' distribution's ep is the first. iter_entry_points
        # yields them in unspecified order.
        all_eps = sorted(
            pkg_resources.iter_entry_points(WIDGETS_ENTRY),
            key=lambda ep:
                0 if ep.dist.project_name.lower() == "arithmos" else 1
        )
        return iter(all_eps)

    @staticmethod
    def addon_entry_points():
        return Config.widgets_entry_points()

    @staticmethod
    def addon_defaults_list(session=None):
        # type: (Optional[requests.Session]) -> List[Dict[str, Any]]
        """
        Return a list of available add-ons.
        """
        if session is None:
            session = requests.Session()
        return session.get(OFFICIAL_ADDON_LIST).json()

    @staticmethod
    def core_packages():
        # type: () -> List[str]
        """
        Return a list of 'core packages'

        These packages constitute required the application framework. They
        cannot be removes via the 'Add-on/plugins' manager. They however can
        be updated. The package that defines the application's `main()` entry
        point must always be in this list.
        """
        return ["Arithmos >=3.20,<4.0a"]

    @staticmethod
    def examples_entry_points():
        # type: () -> Iterable[pkg_resources.EntryPoint]
        """
        Return an iterator over the entry points yielding 'Example Workflows'
        """
        # `iter_entry_points` yields them in unspecified order, so we insert
        # our first
        default_ep = pkg_resources.EntryPoint(
            "Arithmos", "Arithmos.canvas.workflows",
            dist=pkg_resources.get_distribution("Arithmos"))

        return itertools.chain(
            (default_ep,),
            pkg_resources.iter_entry_points("arithmos.widgets.tutorials")
        )

    APPLICATION_URLS = {
        #: Submit a bug report action in the Help menu
        "Bug Report": "https://github.com/biolab/arithmos/issues",
        #: A url quick tour/getting started url
        "Quick Start": "https://arithmos.biolab.si/getting-started/",
        #: The 'full' documentation, should be something like current /docs/
        #: but specific for 'Visual Programing' only
        "Documentation": "https://arithmos.biolab.si/widget-catalog/",
        #: YouTube tutorials
        "Screencasts":
            "https://www.youtube.com/watch"
            "?v=HXjnDIgGDuI&list=PLmNPvQr9Tf-ZSDLwOzxpvY-HrE0yv-8Fy&index=1",
        #: Used for 'Submit Feedback' action in the help menu
        "Feedback": "https://arithmos.biolab.si/survey/long.html",
    }


def init():
    # left for backwards compatibility
    raise RuntimeError("This is not the init you are looking for.")


def data_dir():
    """
    Return the Arithmos application data directory. If the directory path
    does not yet exists then create it.
    """
    from Arithmos.misc import environ
    path = os.path.join(environ.data_dir(), "canvas")
    try:
        os.makedirs(path, exist_ok=True)
    except OSError:
        pass
    return path


def cache_dir():
    """
    Return the Arithmos application cache directory. If the directory path
    does not yet exists then create it.
    """
    from Arithmos.misc import environ
    path = os.path.join(environ.cache_dir(), "canvas")
    try:
        os.makedirs(path, exist_ok=True)
    except OSError:
        pass
    return path


def log_dir():
    """
    Return the application log directory.
    """
    if sys.platform == "darwin":
        name = Config.ApplicationName
        logdir = os.path.join(os.path.expanduser("~/Library/Logs"), name)
    else:
        logdir = data_dir()

    try:
        os.makedirs(logdir, exist_ok=True)
    except OSError:
        pass
    return logdir


def widget_settings_dir():
    """
    Return the widget settings directory.

    .. deprecated:: 3.23
    """
    warnings.warn(
        f"'{__name__}.widget_settings_dir' is deprecated.",
        DeprecationWarning, stacklevel=2
    )
    import arithmoswidget.settings
    return arithmoswidget.settings.widget_settings_dir()


def widgets_entry_points():
    return Config.widgets_entry_points()


def addon_entry_points():
    return Config.addon_entry_points()


def splash_screen():
    return Config.splash_screen()


def application_icon():
    return Config.application_icon()
