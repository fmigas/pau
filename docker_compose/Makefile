
start-redpanda:
	docker compose -f redpanda.yml up -d

stop-redpanda:
	docker compose -f redpanda.yml down

start-feature-pipeline:
	docker compose -f feature_pipeline.yml up --build -d

stop-feature-pipeline:
	docker compose -f feature_pipeline.yml down

start-historical-pipeline:
	#docker compose -f historical_pipeline.yml up -d
	docker compose -f historical_pipeline.yml up --build -d

stop-historical-pipeline:
	docker compose -f historical_pipeline.yml down

# check health of our production API
check-health-prod:
	curl -X GET https://price-predictor-824943a-fmigaszewski-pau-production.deployments.quix.io/health

# make a prediction request to our production API
predict-request-prod:
	curl -X GET https://price-predictor-824943a-fmigaszewski-pau-production.deployments.quix.io/predict?product_id=BTC%2FUSD

check-health-dev:
	curl -X GET https://price-predictor-824943a-fmigaszewski-pau-dev.deployments.quix.io/health

predict-request-dev:
	curl -X GET https://price-predictor-824943a-fmigaszewski-pau-dev.deployments.quix.io/predict?product_id=BTC%2FUSD
