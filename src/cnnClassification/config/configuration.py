import os
from pathlib import Path
from cnnClassification.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from cnnClassification.utils.common import read_yaml, create_directories
from cnnClassification.entity.config_entity import DataIngestionConstants

class ConfigurationManager:
    def __init__(
        self,
        config_filepath: Path = CONFIG_FILE_PATH,
        params_filepath: Path = PARAMS_FILE_PATH,
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConstants:
        config = self.config.data_ingestion

        data_ingestion_constants = DataIngestionConstants(
            root_dir=Path(config.root_dir),
            tumor_dir=Path(config.tumor_dir),
            normal_dir=Path(config.normal_dir),
            train_dir=Path(config.train_dir),
            test_dir=Path(config.test_dir),
            test_size=config.test_size,
        )

        return data_ingestion_constants
