from fastapi import FastAPI, HTTPException, Query
# from pydantic import BaseModel
# import joblib

from loguru import logger

# from hopsworks_api import push_value_to_feature_group
from src.config import config
from src.price_predictor import PricePredictor

app = FastAPI()

# we have one object per product id
predictors: dict[str, PricePredictor] = {}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/predict")
def predict(product_id: str = Query(..., description = "The product ID to predict")):

    logger.info(f"Received request for product id: {product_id}")

    try:
        if product_id not in config.api_supported_product_ids.split(","):
            raise HTTPException(status_code = 400, detail = "Product ID not supported")

        # if we don't have the predictor for this product id, we create it
        if product_id not in predictors:
            logger.info(f"Loading model for product id {product_id} from Comet")
            predictors[product_id] = PricePredictor.from_model_registry(
                product_id = product_id,

                # these are read from the config file
                # the end user doesn't have to provide them
                ohlc_window_sec = config.ohlc_window_sec,
                forecast_steps = config.forecast_steps,
                status = config.ml_model_status,
            )
        logger.info(f"Model loaded from Comet")

        # extract the predictor object for this product id
        predictor = predictors[product_id]
        logger.info(f"Predictor for product id {product_id} loaded from Comet")

        # the ML magic happens here
        prediction = predictor.predict()
        logger.info(f"Prediction for product id {product_id} done")

        return {"prediction": prediction.to_json()}
        # return prediction.to_json()

    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))
