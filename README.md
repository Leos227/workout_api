<p align="center">
  <img src="assets/banner.svg" alt="Workout API banner" width="100%" />
</p>

<p align="center">
  <a href="https://www.python.org/">
    <img alt="Python" src="https://img.shields.io/badge/Python-3.10+-ff6a00?style=for-the-badge&labelColor=000000">
  </a>
  <a href="#">
    <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-⚡-ff6a00?style=for-the-badge&labelColor=000000">
  </a>
  <a href="#">
    <img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-14-ff6a00?style=for-the-badge&labelColor=000000">
  </a>
</p>

> **Workout API** — Admin de atletas para eventos de CrossFit.  
> Cadastre participantes, vincule **categorias/divisões** e **centros de treinamento (box)**. Simples, rápido, sem burpee extra.

---

## 🔧 Setup
```bash
# 1) Banco
docker compose up -d db

# 2) Ambiente Python
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# 3) Variáveis de ambiente
cp .env.example .env  # edite se precisar

# 4) Migrações
alembic upgrade head

# 5) API
uvicorn workout_api.main:app --reload   # http://localhost:8000/docs

