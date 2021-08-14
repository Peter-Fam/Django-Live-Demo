#!/usr/bin/env bash
while !</dev/tcp/db/5432; do
	sleep 0.1
done
python manage.py migrate
python manage.py collectstatic --no-input --clear

exec "$@"
