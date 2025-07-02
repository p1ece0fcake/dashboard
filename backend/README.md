# Backend

Minimal FastAPI backend for the dashboard application.

## Development

Create virtualenv and install dependencies:

```bash
python -m venv venv
source venv/bin/activate
pip install fastapi uvicorn sqlalchemy pydantic
```

Initialize database and run server:

```bash
python -m backend.app.db.init_db
uvicorn backend.app.main:app --reload
```
