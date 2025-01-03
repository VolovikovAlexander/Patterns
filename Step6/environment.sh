#!/bin/bash

python3 -m venv .venv
. .venv/bin/activate

pip3 install typing-extensions --upgrade
pip3 install dict2xml
pip3 install -U connexion[flask]
pip3 install -U connexion[swagger-ui]
pip3 install -U connexion[uvicorn]
pip3 install -U flask-restplus
pip3 install -U Flask