#!/bin/bash

clear
export FLASK_DEBUG=1
export FLASK_APP=dns301.py
python -m flask run