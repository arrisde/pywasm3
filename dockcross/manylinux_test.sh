#!/usr/bin/env bash
set -ef -o pipefail

VER=$1
PY=/opt/python/${VER}/bin/python
${PY} -m venv /tmp/.venv
source /tmp/.venv/bin/activate
WHLFIND="find ./dist/ -name *${VER}*.whl"
WHL=`${WHLFIND}`
python -m pip install -I $WHL

python -m unittest discover