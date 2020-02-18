#!/bin/bash

gunicorn "auth:create_app()" \
    -c gunicorn.conf.py \
