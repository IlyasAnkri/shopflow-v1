build:
	docker compose build

up:
	docker compose up -d

test:
	pytest test_api.py -v

down:
	docker compose down
