
build:
	docker build -t trade-producer .

run-prod-live: build
	docker run \
		--env-file live.prod.env \
		--network=redpanda_network trade-producer

run-prod-live-detatched: build
	docker run -d \
		--env-file live.prod.env \
		--network=redpanda_network trade-producer

run-prod-historical: build
	docker run \
		--env-file historical.prod.env \
		--network=redpanda_network trade-producer

run-prod-historical-detatched: build
	docker run -d \
		--env-file historical.prod.env \
		--network=redpanda_network trade-producer


run-dev-live:
	cp live.dev.env .env
	poetry run python src/main.py

run-dev-historical:
	cp historical.dev.env .env
	poetry run python src/main.py


start-redpanda:
	docker compose -f redpanda.yml up -d

stop-redpanda:
	docker compose -f redpanda.yml down