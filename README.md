# Workout API

API REST para administrar **participantes de competições de CrossFit**.  
Permite cadastrar atletas, organizar por **categorias/divisões** e associar cada atleta ao seu **centro de treinamento (box/afiliado)**.

## Objetivo

- **Inscrição** e gestão de atletas (dados pessoais e métricas físicas básicas).
- **Organização** por divisões de competição (ex.: *Scale*, *RX/Elite*, *Master*).
- **Vínculo** do atleta a um box/centro (para estatísticas por afiliado).

> Escopo atual: *Atletas*, *Categorias*, *Centros de Treinamento*.  
> Próximos passos sugeridos: Heats, Workouts (WODs), Heats Assignment e Leaderboard.

---

## Stack

- **FastAPI** (Python 3.10+)
- **SQLAlchemy Async** + `asyncpg`
- **PostgreSQL** (Docker Compose)
- **Alembic** (migrações)

---

## Como rodar

```bash
# 1) Banco
docker compose up -d db

# 2) Ambiente Python
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# 3) Variáveis de ambiente
cp .env.example .env

# 4) Migrações
alembic upgrade head

# 5) API
uvicorn workout_api.main:app --reload  # http://localhost:8000/docs
