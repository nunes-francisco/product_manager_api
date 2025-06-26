run:
	docker-compose up --build

test:
	pytest tests/

migrate:
	autoflake --remove-all-unused-imports -i -r . && alembic upgrade head
