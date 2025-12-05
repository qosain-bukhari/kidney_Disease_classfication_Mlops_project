import os
import shutil
from pathlib import Path
from sklearn.model_selection import train_test_split
from cnnClassification.entity.config_entity import DataIngestionConstants
from cnnClassification.utils.common import create_directories, logger

class DataIngestion:
    def __init__(self, config: DataIngestionConstants):
        self.config = config
        create_directories([self.config.train_dir, self.config.test_dir])

    def ingest_data(self):
        """
        Copies images from local tumor/normal folders into train/test directories.
        """
        for category in ["tumor", "normal"]:
            src_dir = getattr(self.config, f"{category}_dir")
            files = os.listdir(src_dir)
            train_files, test_files = train_test_split(files, test_size=self.config.test_size, random_state=42)
            
            for file in train_files:
                shutil.copy(os.path.join(src_dir, file), os.path.join(self.config.train_dir, category + "_" + file))
            for file in test_files:
                shutil.copy(os.path.join(src_dir, file), os.path.join(self.config.test_dir, category + "_" + file))
        
        logger.info("Data ingestion completed successfully.")
