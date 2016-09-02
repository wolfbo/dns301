#!/bin/bash

clear
echo "installing python-virtualenv"
pip install virtualenv

echo "initialising virtualenv"
virtualenv virtualenv

echo "activating virtualenv"
source virtualenv/bin/activate

echo "installing requirements into virtualenv"
pip install -r requirements.txt

export PORT=5000
export FLASK_DEBUG=1
export FLASK_APP=dns301.py

echo "starting flaskapp on port $PORT"
python -m flask run --port $PORT