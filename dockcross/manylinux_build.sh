#!/usr/bin/env bash
set -ef -o pipefail # older venv doesnt support -u

VER=$1 # currently dockcross supports cp35-cp35m, cp36-cp36m, cp37-cp37m, cp38-cp38 
PY=/opt/python/${VER}/bin/python
${PY} -m venv /tmp/.venv
source /tmp/.venv/bin/activate
python -m pip install -r requirements.txt
python setup.py bdist_wheel