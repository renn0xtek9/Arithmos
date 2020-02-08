"""

"""
import os
import sysconfig

import pkg_resources

import Arithmos


# Entry point for main Arithmos categories/widgets discovery
def widget_discovery(discovery):
    dist = pkg_resources.get_distribution("Arithmos")
    pkgs = [
        "Arithmos.widgets.data",
        "Arithmos.widgets.visualize",
        "Arithmos.widgets.model",
        "Arithmos.widgets.evaluate",
        "Arithmos.widgets.unsupervised",
    ]
    for pkg in pkgs:
        discovery.process_category_package(pkg, distribution=dist)


WIDGET_HELP_PATH = (
    ("{DEVELOP_ROOT}/doc/visual-programming/build/htmlhelp/index.html", None),
    (os.path.join(sysconfig.get_path("data"),
                  "share/help/en/arithmos/htmlhelp/index.html"),
     None),
    ("https://docs.arithmos.biolab.si/3/visual-programming/", ""),
)
