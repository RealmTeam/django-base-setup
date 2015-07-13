#!/bin/bash
set -e

if [ "$1" = 'start' ]; then
    cd /app
    exec gunicorn -w ${NUM_WORKERS:-2} -t ${TIMEOUT:-120} \
                  --log-level=info \
                  -b 0.0.0.0:8000 \
                  base.wsgi:application
fi

exec "$@"
