# This configuration file is a python module
# This is code that reads config.yaml and prepares Python objects from it.
# Parses the raw YAML into Python objects (Entities)
# Provides helper methods (get_prepare_base_model_config(), get_training_config(), …) so each pipeline step gets the correct config object.

from cnnChickenDiseaseClassifier.constants import *
from cnnChickenDiseaseClassifier.utils.common import read_yaml, create_directories
from cnnChickenDiseaseClassifier.entity.config_entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root]) # = "create_directories(["artifacts"])""
        # ^ we can use the . here instead of [artifacts] because, remember, read_yaml returns a Box Type (this is exactly why we made it return ConfigBox)


    
    def get_data_ingestion_config(self) -> DataIngestionConfig: # here, we're making it return a DataIngestionConfig type, which we defined earlier as an Entity (structure) for data ingestion configuration
        config = self.config.data_ingestion 

        create_directories([config.root_dir]) # will create artifacts/data_ingestion as specified in config.yaml

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config