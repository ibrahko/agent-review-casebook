# shop-api

A small order API (Django + Django REST framework).

```
uv sync
uv run python manage.py migrate
uv run python manage.py seed_demo
uv run python manage.py runserver
```

Then open http://127.0.0.1:8000/api/orders/

Tests: `uv run python manage.py test`
