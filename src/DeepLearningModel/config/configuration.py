from DeepLearningModel.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from DeepLearningModel.utils import read_yaml, create_directories
from DeepLearningModel.entity import DataIngestionConfig

# The Configration manager is responsible for holding the methods that are used to 
# a) Create nessesary folder structure in root for each component's config object
# b) Assigning values to Configs which are defined in entity by reading input from config.yaml and returning config object 

class ConfigurationManager:
    # The constructor will read config.yaml and params.yaml and will ceate nessesary folder for artifacts
    def __init__(self, config_filepath = CONFIG_FILE_PATH, params_filepath = PARAMS_FILE_PATH):
        print(config_filepath)
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        print(params_filepath)
        create_directories([self.config.artifacts_root])

    # The get_data_ingestion_config function will 
    # a) Read config values from config.yaml
    # b) Will create folder in artifact for data ingestion config object
    # c) Assign the values to DataIngestionConfig object and return it
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config