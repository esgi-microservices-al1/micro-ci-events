#!/bin/sh
exec gunicorn app:app -b 0.0.0.0:5000 -w 4 --threads=4 --worker-class=gthread