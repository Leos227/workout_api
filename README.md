<p align="center">
  <img src="./assets/banner.svg" alt="Workout API banner" width="100%" />
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-ff6a00?style=for-the-badge&labelColor=0a0a0a">
  <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-async-ff6a00?style=for-the-badge&labelColor=0a0a0a">
  <img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-14-ff6a00?style=for-the-badge&labelColor=0a0a0a">
</p>

> Admin de **participantes de CrossFit** — atletas, categorias (divisões) e centros de treinamento (box). Rápido, direto, sem firula.

## 🔧 Setup

```bash
docker compose up -d db
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
alembic upgrade head
uvicorn workout_api.main:app --reload  # http://localhost:8000/docs


