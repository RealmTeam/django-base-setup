#!/bin/bash
set -e

cd /app
python manage.py migrate

if [ "$1" = 'start' ]; then
    exec gunicorn -w ${NUM_WORKERS:-2} -t ${TIMEOUT:-120} \
                  --log-level=info \
                  --access-logfile=- \
                  --error-logfile=- \
                  -b 0.0.0.0:8000 \
                  main.wsgi:application
fi

if [ "$1" = 'celery' ]; then
    exec celery --app=main.celery:app worker -B --loglevel=INFO
fi

exec "$@"
