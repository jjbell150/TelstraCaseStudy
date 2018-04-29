#!/bin/sh
export FLASK_APP=./index.py
source $(pipenv --venv)/scripts/activate
flask run -h 0.0.0.0