run:
	@uvicorn workout_api.main:app --reload --host 0.0.0.0 --port 8000

create-migrations:
	@if [ -z "$(d)" ]; then echo "❌ Informe uma mensagem: make create-migrations d=mensagem"; exit 1; fi
	@PYTHONPATH=$$PYTHONPATH:$(pwd) alembic revision --autogenerate -m "$(d)"

run-migrations:
	@PYTHONPATH=$$PYTHONPATH:$(pwd) alembic upgrade head


