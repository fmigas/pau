import pytest
from src.main import update_ohlcv_candle


def test_updates_high_price():
    candle = {'high': 100, 'low': 90, 'close': 95, 'volume': 10, 'product_id': 'BTC'}
    trade = {'price': 105, 'quantity': 5, 'product_id': 'BTC'}
    updated_candle = update_ohlcv_candle(candle, trade)
    assert updated_candle['high'] == 105


def test_updates_low_price():
    candle = {'high': 100, 'low': 90, 'close': 95, 'volume': 10, 'product_id': 'BTC'}
    trade = {'price': 85, 'quantity': 5, 'product_id': 'BTC'}
    updated_candle = update_ohlcv_candle(candle, trade)
    assert updated_candle['low'] == 85


def test_updates_close_price():
    candle = {'high': 100, 'low': 90, 'close': 95, 'volume': 10, 'product_id': 'BTC'}
    trade = {'price': 97, 'quantity': 5, 'product_id': 'BTC'}
    updated_candle = update_ohlcv_candle(candle, trade)
    assert updated_candle['close'] == 97


def test_updates_volume():
    candle = {'high': 100, 'low': 90, 'close': 95, 'volume': 10, 'product_id': 'BTC'}
    trade = {'price': 97, 'quantity': 5, 'product_id': 'BTC'}
    updated_candle = update_ohlcv_candle(candle, trade)
    assert updated_candle['volume'] == 15


def test_retains_product_id():
    candle = {'high': 100, 'low': 90, 'close': 95, 'volume': 10, 'product_id': 'BTC'}
    trade = {'price': 97, 'quantity': 5, 'product_id': 'BTC'}
    updated_candle = update_ohlcv_candle(candle, trade)
    assert updated_candle['product_id'] == 'BTC'
