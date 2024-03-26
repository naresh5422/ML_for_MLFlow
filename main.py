from ML_Project import logger
from ML_Project.pipeline.stage_1_Data_ingestion import DataIngestinTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"


try:
    logger.info(f">>>>> stage {STAGE_NAME} started<<<<<")
    obj = DataIngestinTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} Completed<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e