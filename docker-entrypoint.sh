#!/bin/bash

set -e

cd /opt/auth

# gunicorn启动命令
gunicorn auth:app \
        --bind 0.0.0.0:8000 \
        --workers 4 \
         --worker-class=gevent --daemon=true
exec "$@"