training-dev:
	poetry run python src/training.py

prediction-dev:
	poetry run python src/prediction.py

build:
	docker build -t price_predictor_training .

#run: build
#	docker run --env-file .env price_predictor_training

training: build
	docker run \
		--env-file .env \
		-e TRAINING_OR_PREDICTION=training \
		price_predictor_training

api: build
	docker run \
		-p 8000:80 \
		--env-file .env \
		-e TRAINING_OR_PREDICTION=prediction \
		price_predictor_api


test:
	poetry run python tests/hopsworks_test.py
