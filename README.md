# Eisenhower Matrix Django App

A deployable Django app for organizing tasks in an Eisenhower Matrix:

- **Do** (Urgent + Important)
- **Schedule** (Not Urgent + Important)
- **Delegate** (Urgent + Not Important)
- **Eliminate** (Not Urgent + Not Important)

## Features

- Create, update, delete tasks
- Toggle task completion
- Grouped board view by quadrant
- Django admin for management
- Production settings ready for Gunicorn + WhiteNoise + Postgres

## Quick Start (Local)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Or run:

```bash
./scripts/run_local.sh
```

Then open `http://127.0.0.1:8000`.

## Deployment

### Option A: Generic Linux VM

```bash
git clone <your-repo-url>
cd eisenhower
cp .env.example .env
# edit .env for production values
./scripts/deploy.sh
```

Start app:

```bash
gunicorn eisenhower_project.wsgi --bind 0.0.0.0:8000
```

Use Nginx/Caddy as a reverse proxy and set `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS`.

### Option B: Heroku / Render-style PaaS

This repo includes:

- `Procfile` for web + release commands
- `runtime.txt` for Python runtime

Set env vars in your platform:

- `SECRET_KEY`
- `DEBUG=False`
- `ALLOWED_HOSTS`
- `CSRF_TRUSTED_ORIGINS`
- `DATABASE_URL` (managed Postgres URL)

Deploy by connecting your repo to the platform.

## Environment Variables

- `SECRET_KEY`: Django secret key
- `DEBUG`: `True`/`False`
- `ALLOWED_HOSTS`: Comma-separated hosts
- `CSRF_TRUSTED_ORIGINS`: Comma-separated origins (with scheme)
- `DATABASE_URL`: e.g. `postgres://...` or `sqlite:///db.sqlite3`
- `TIME_ZONE`: defaults to `UTC`

## Project Structure

- `eisenhower_project/` Django project settings and entrypoints
- `matrix/` App with models/views/forms/templates
- `scripts/` Deployment and local run scripts

## Notes

- Static assets are served using WhiteNoise.
- Run `python manage.py collectstatic --noinput` before production start.
