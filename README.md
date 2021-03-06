<kbd height=36><img src=https://raw.githubusercontent.com/irgolic/arithmos/master/distribute/icon-48.png alt=img height=36/></kbd> Arithmos
======

[![Discord Chat](https://img.shields.io/discord/633376992607076354?style=for-the-badge&logo=discord&color=arithmos&labelColor=black)](https://discord.gg/FWrfeXV)
[![build: passing](https://img.shields.io/travis/biolab/arithmos?style=for-the-badge&labelColor=black)](https://travis-ci.org/biolab/arithmos)
[![codecov](https://img.shields.io/codecov/c/github/biolab/arithmos?style=for-the-badge&labelColor=black)](https://codecov.io/gh/biolab/arithmos)

[Arithmos] is a component-based data mining software. It includes a range of data
visualization, exploration, preprocessing and modeling techniques. It can be
used through a nice and intuitive user interface or, for more advanced users,
as a module for the Python programming language.

This is the latest version of Arithmos (for Python 3). The deprecated version of Arithmos 2.7 (for Python 2.7) is still available ([binaries] and [sources]).

[Arithmos]: https://arithmos.biolab.si/
[binaries]: https://arithmos.biolab.si/arithmos2/
[sources]: https://github.com/biolab/arithmos2


Installing with Miniconda / Anaconda
------------------------------------

Arithmos requires Python 3.6 or newer.

First, install [Miniconda] for your OS. Create virtual environment for Arithmos:

    conda create python=3 --name arithmos

In your Anaconda Prompt add conda-forge to your channels:pip3

    conda config --add channels conda-forge

This will enable access to the latest Arithmos release. Then install Arithmos:

    conda install arithmos

[Miniconda]: https://docs.conda.io/en/latest/miniconda.html

To install the add-ons, follow a similar recipe:

    conda install arithmos-<addon name>

See specific add-on repositories for details.

Installing with pip
-------------------

To install Arithmos with pip, run the following.

    # Install some build requirements via your system's package manager
    sudo apt install virtualenv build-essential python3-dev

    # Create a separate Python environment for Arithmos and its dependencies ...
    virtualenv --python=python3 --system-site-packages arithmosvenv
    # ... and make it the active one
    source arithmosvenv/bin/activate

    # Install Qt dependencies for the GUI
    pip install PyQt5 PyQtWebEngine

    # Install Arithmos
    pip install arithmos

Starting Arithmos GUI
-------------------

To start Arithmos GUI from the command line, run:

    arithmos-canvas
    # or
    python3 -m Arithmos.canvas

Append `--help` for a list of program options.
