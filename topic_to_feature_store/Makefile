run-live-dev:
	cp live.dev.env .env
	poetry run python src/main_new.py

run-historical:
	cp historical.dev.env .env
	poetry run python src/main_new.py


build:
	docker build -t topic-to-feature-store .

run-live:
	docker run \
		--env-file live.prod.env \
		--network=redpanda_network topic-to-feature-store


run-live-detatched:
	docker run -d \
		--env-file live.prod.env \
		--network=redpanda_network topic-to-feature-store


run-historical-prod:
	docker run \
		--env-file historical.prod.env \
		--env-file credentials.env \
		--network=redpanda_network topic-to-feature-store


run-historical-detatched:
	docker run -d \
		--env-file historical.prod.env \
		--env-file credentials.env \
		--network=redpanda_network topic-to-feature-store

