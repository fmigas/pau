training-dev:
	poetry run python src/training.py

prediction-dev:
	poetry run python src/prediction.py

build:
	docker build -t price_predictor .

#run: build
#	docker run --env-file .env price_predictor_training

training: build
	docker run \
		--env-file .env \
		-e TRAINING_OR_PREDICTION=training \
		price_predictor

api:
	docker run \
		-p 8000:80 \
		--env-file .env \
		-e TRAINING_OR_PREDICTION=prediction \
		price_predictor


test:
	poetry run python tests/hopsworks_test.py

request:
	curl "http://0.0.0.0:80/?product_id=BTC%2FUSD"


test:
	poetry run pytest