#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Convert static assets to a production-ready format
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate