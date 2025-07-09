#!/bin/bash
# Entrypoint script to prepare the environment for Django

# Wait for the database to be ready
until nc -z -v -w30 jb-p1-db 5432
do
  echo "Waiting for database connection..."
  sleep 1
done

python manage.py migrate

exec "$@"