

from src.ohlc_data_reader import OhlcDataReader
from src.config import hopsworks_config


ohlc_data_reader = OhlcDataReader(
    ohlc_window_sec = 60,
    hopsworks_config = hopsworks_config,
    feature_view_name = 'ohlcv_feature_view',
    feature_view_version = 1,
    feature_group_name = 'ohlcv_feature_group',
    feature_group_version = 1,
)

# check if reading from the online store works
# output = ohlc_data_reader.read_from_online_store(
#     product_id = 'BTC/USD',
#     last_n_minutes = 20,
# )


# logger.debug(f'Live OHLC data: {output}')

# check if reading from the offline store works
# output = ohlc_data_reader.read_from_offline_store(
#     product_id = 'BTC/USD',
#     last_n_days = 90,
# )
# logger.debug(f'Historical OHLC datasize: {output.shape}')
# output.to_csv('ohlc_data.csv', index = False)

output = ohlc_data_reader.read_from_online_store(
    product_id = 'BTC/USD',
    last_n_minutes = 50,
)

