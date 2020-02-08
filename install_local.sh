#!/bin/bash
set -e
cd $HOME
sudo apt install virtualenv build-essential python3-dev -y
virtualenv --python=python3 --system-site-packages orange3venv
source orange3venv/bin/activate
pip install PyQt5 PyQtWebEngine
pip install orange3
orange-canvas

