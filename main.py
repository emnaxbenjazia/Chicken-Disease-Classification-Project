from cnnChickenDiseaseClassifier import logger
from cnnChickenDiseaseClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion stage"
if __name__ == '__main__':  
    try:
        # Log the start of the current pipeline stage
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        # Create an instance of the pipeline class for this stage (data ingestion in our case)
        obj = DataIngestionTrainingPipeline()
        # Run the main logic of this pipeline stage (download + extract dataset)
        obj.main()
        # Log the successful completion of this stage
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    
    except Exception as e:
        # If an error occurs, log the full exception details
        logger.exception(e)
        # Re-raise the exception so the program stops instead of failing silently
        raise e
