from ML_Project.config.configuration import ConfigurationManager
from ML_Project.components.data_ingestion import DataIngestion
from ML_Project import logger

STAGE_NAME = "data ingestion stage"

class DataIngestinTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()



if __name__=="__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started<<<<<")
        obj = DataIngestinTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} Completed<<<<<\n\nx==========x")
    except Exception as e:
        raise e