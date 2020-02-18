#!/bin/bash

gunicorn "auth:create_app()" \
    -c gunicorn.conf.py \
    --access-logfile "/home/amber/eForm-Backend/logs/eForm-Auth-0.log" \
    --error-logfile "/home/amber/eForm-Backend/logs/eForm-Auth-0.error.log" \
    --log-level info
