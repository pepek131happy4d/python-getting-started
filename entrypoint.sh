#!/bin/sh

python3 manage.py

# check wheterh port is null
if [ -z "$PORT" ]; then
    PORT=5000
fi
gunicorn --bind 0.0.0.0:${PORT} wsgi 
