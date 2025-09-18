<p align="center">
  <img src="./assets/banner.svg" alt="Workout API banner" width="100%"/>
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-ff6a00?style=for-the-badge&labelColor=0a0a0a">
  <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-async-ff6a00?style=for-the-badge&labelColor=0a0a0a">
  <img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-14-ff6a00?style=for-the-badge&labelColor=0a0a0a">
</p>

---

## 📖 Sobre o projeto
Workout API é uma aplicação desenvolvida para a gestão de **participantes de CrossFit**, permitindo o cadastro e administração de atletas, categorias (divisões) e centros de treinamento (boxes).  
O sistema foi construído com foco em **desempenho, clareza e escalabilidade**.

---

## ✨ Funcionalidades
- Cadastro e gerenciamento de atletas  
- Organização por categorias/divisões  
- Controle de centros de treinamento (boxes)  
- Documentação interativa via Swagger/OpenAPI  
- Banco de dados PostgreSQL com migrações automatizadas (Alembic)  

---

## 🚀 Instalação e execução

```bash
# 1. Subir o banco de dados
docker compose up -d db

# 2. Criar ambiente virtual e instalar dependências
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Configurar variáveis de ambiente
cp .env.example .env

# 4. Executar migrações
alembic upgrade head

# 5. Iniciar servidor
uvicorn workout_api.main:app --reload
