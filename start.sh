#!/bin/bash
cd /app
/usr/local/bin/gunicorn --bind 0.0.0.0:8002 historystate.wsgi:application 