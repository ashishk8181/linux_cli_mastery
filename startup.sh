#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
# python manage.py migrate --noinput

# Start server (Daphne is auto-used via ASGI_APPLICATION setting)
daphne -b 0.0.0.0 -p 8000 linux_cli_mastery.asgi:application
