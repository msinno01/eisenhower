#!/usr/bin/env bash
set -euo pipefail

if [[ -f .env ]]; then
  set -a
  source .env
  set +a
fi

python manage.py migrate
python manage.py runserver 0.0.0.0:${PORT:-8000}
