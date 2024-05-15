#!/bin/bash

python3 manage.py migrate
python3 manage.py compilemessages

gunicorn -b 0.0.0.0:8000 enzopbme.wsgi