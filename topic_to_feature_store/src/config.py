from typing import List, Optional

from pydantic_settings import BaseSettings
from typing import List, Optional
# hej

class AppConfig(BaseSettings):
    kafka_broker_address: Optional[str] = None
    kafka_input_topic: str
    kafka_consumer_group: str

    feature_group_name: str
    feature_group_version: int
    feature_group_primary_keys: List[str]
    feature_group_event_time: str
    start_offline_materialization: bool
    batch_size: Optional[int] = 1
    read_from_beginning: Optional[bool] = False

    class Config:
        env_file = ".env"


class HopsworksConfig(BaseSettings):
    hopsworks_project_name: str
    hopsworks_api_key: str

    class Config:
        env_file = "credentials.env"


config = AppConfig()
hopsworks_config = HopsworksConfig()
