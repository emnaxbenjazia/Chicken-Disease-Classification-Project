from cnnChickenDiseaseClassifier.config.configuration import ConfigurationManager
from cnnChickenDiseaseClassifier.components.data_ingestion import DataIngestion 
from cnnChickenDiseaseClassifier import logger 


STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self): # the pipeline itself
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


# In the DVC context, this block is what gets executed when DVC runs the stage (cmd: python stage_01_data_ingestion.py).
# Ensures this block only runs when the script is executed directly (not when imported as a module)
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

