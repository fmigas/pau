import pytest
import pandas as pd
from src.utils import hash_dataframe, timestamp_ms_to_human_readable_utc


def test_hash_dataframe_returns_consistent_hash():
    df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    hash1 = hash_dataframe(df)
    hash2 = hash_dataframe(df)
    assert hash1 == hash2


def test_timestamp_ms_to_human_readable_utc_converts_correctly():
    timestamp_ms = 1609459200000  # 2021-01-01 00:00:00 UTC
    result = timestamp_ms_to_human_readable_utc(timestamp_ms)
    assert result == "2021-01-01 00:00:00 UTC"


def test_timestamp_ms_to_human_readable_utc_handles_epoch():
    timestamp_ms = 0  # 1970-01-01 00:00:00 UTC
    result = timestamp_ms_to_human_readable_utc(timestamp_ms)
    assert result == "1970-01-01 00:00:00 UTC"


def test_timestamp_ms_to_human_readable_utc_handles_negative_timestamp():
    timestamp_ms = -1  # 1969-12-31 23:59:59 UTC
    result = timestamp_ms_to_human_readable_utc(timestamp_ms)
    assert result == "1969-12-31 23:59:59 UTC"
