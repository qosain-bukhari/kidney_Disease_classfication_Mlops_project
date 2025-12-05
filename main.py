

from cnnClassification.config.configuration import ConfigurationManager
from cnnClassification.components.data_ingestion import DataIngestion
from cnnClassification.utils.common import logger

def main():
    try:
        # Step 1: Initialize Configuration Manager
        config_manager = ConfigurationManager()
        logger.info("Configuration Manager initialized.")

        # Step 2: Get Data Ingestion configuration
        data_ingestion_config = config_manager.get_data_ingestion_config()
        logger.info(f"Data Ingestion Config: {data_ingestion_config}")

        # Step 3: Run Data Ingestion
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.ingest_data()

        logger.info("Data ingestion pipeline completed successfully.")

    except Exception as e:
        logger.error(f"Error in main.py: {e}")
        raise e

if __name__ == "__main__":
    main()
