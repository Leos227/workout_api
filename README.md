# README
cat > README.md << 'EOF'
# Workout API

FastAPI + SQLAlchemy Async + Postgres + Alembic.

## Como rodar
```bash
docker compose up -d db
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
alembic upgrade head
uvicorn workout_api.main:app --reload  # http://localhost:8000/docs
