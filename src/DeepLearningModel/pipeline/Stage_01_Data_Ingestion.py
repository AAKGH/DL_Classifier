import os
from DeepLearningModel.config.configuration import ConfigurationManager
from DeepLearningModel.components.Data_Ingestion import DataIngestion
from DeepLearningModel import logger

STAGE_NAME = 'Data Ingestion Stage'

def main() :
    try:
        os.chdir("c:\\Users\\AK\\DL_CLASSIFIER")
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.unzip_and_clean()
    except Exception as e:
        raise e

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>> {STAGE_NAME} started<<<<<<<<<<<<<<<<")
        main()
        logger.info(f">>>>>>>>>>>>>>>>>>> {STAGE_NAME} completed<<<<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e   