#!/bin/sh
echo "$DB_HOST"
echo "$DATABASE"
flask init-db
echo 'Iniciando servidor...'
# exec gunicorn -b :5000 --access-logfile - --error-logfile - app:app
exec "$@"
