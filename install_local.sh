#!/bin/bash
set -e
cd $HOME
sudo apt install virtualenv build-essential python3-dev -y
virtualenv --python=python3 --system-site-packages arithmosvenv
source arithmosvenv/bin/activate
pip install PyQt5 PyQtWebEngine
# pip install arithmos
pip install Arithmos
arithmos-canvas

