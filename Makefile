include .env

pre-commit:
	pip install pre-commit --upgrade
	pre-commit install

up:
	docker compose up --build -d

logs:
	docker compose logs -f --no-log-prefix backend

down:
	docker compose down

shell-db:
	docker compose exec db psql postgresql://$(POSTGRES_USER):$(POSTGRES_PASSWORD)@$(POSTGRES_SERVER):$(POSTGRES_PORT)/$(POSTGRES_DB)

test:
	docker compose exec backend python -m tests.run

revision:
	docker compose exec backend alembic revision --autogenerate

upgrade:
	docker compose exec backend alembic upgrade head

downgrade:
	docker compose exec backend alembic downgrade head

revision:
	docker compose exec backend alembic revision --autogenerate

upgrade:
	docker compose exec backend alembic upgrade head

downgrade:
	docker compose exec backend alembic downgrade head
