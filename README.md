# Starter Project

An early Django prototype from January 2018.

## Original idea

The intended project was a soccer-match viewer with a timeline scroller. A user would scrub through a match and explore viewpoints from the crowd, using the X, Y, and Z coordinates associated with each viewpoint.

That describes the idea, not the current state of this repository: the timeline and viewpoint viewer were not implemented here.

## What this repository contains

- A small Django site with an `article` app.
- A `Post` model with a title, description, and timestamp.
- A placeholder homepage that says “this is where my content goes.”
- Django's admin page, where post records can be managed.
- A SQLite database with one sample post.

There is no soccer-match data, timeline control, video playback, viewpoint coordinate data, or 3D/game renderer in this copy. The existing Django app is a starter site rather than a working version of the original viewer concept.

## Running the existing site

The original requirements are pinned to Django 2.0.1, released in 2018. They have not been updated or checked against a current Python version, so the commands below may need an older compatible Python environment.

From the project folder:

```bash
python3 -m venv env
source env/bin/activate
python -m pip install -r requirements.txt
cd newproject
python manage.py migrate
python manage.py runserver
```

The homepage is at `http://127.0.0.1:8000/`. The Django admin is at `http://127.0.0.1:8000/admin/` and requires an admin account.
