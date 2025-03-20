#!/bin/sh
handle_error() {
    echo "An error occurred on line $1"
    exit 1
}

trap 'handle_error $LINENO' ERR

echo "Waiting for postgres..."

while ! nc -z "postgres" "5432"; do
    sleep 0.1
done

echo "PostgreSQL started"
flask db migrate
flask db upgrade
python -u app.py