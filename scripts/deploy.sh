#!/usr/bin/env bash
set -euo pipefail

python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate --noinput
python manage.py collectstatic --noinput

echo "Deploy prep complete. Start server with: gunicorn eisenhower_project.wsgi --bind 0.0.0.0:${PORT:-8000}"
