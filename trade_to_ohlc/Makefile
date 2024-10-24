
build:
	docker build -t trade-to-ohlc .

run-live: build
	docker run \
		--env-file live.prod.env \
		--network=redpanda_network trade-to-ohlc

run-detatched-live:
	docker run -d \
		--env-file live.prod.env \
		--network=redpanda_network trade-to-ohlc


run-historical-prod:
	docker run -d \
		--env-file historical.prod.env \
		--network=redpanda_network trade-to-ohlc


run-detatched-historical-prod:
	docker run -d \
		--env-file historical.prod.env \
		--network=redpanda_network trade-to-ohlc

run-dev:
	cp live.dev.env .env
	poetry run python src/main.py

run-dev-historical:
	cp historical.dev.env .env
	poetry run python src/main.py

test:
	poetry run pytest
