# The component takes config object as input
# The component holds all the definations for fuctions associated with execution of activities in a block of pipeline

import os
import urllib.request as request
from zipfile import ZipFile
from DeepLearningModel.entity.config_entity import DataIngestionConfig

class DataIngestion:
    # The constructor will associate config object with component
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    # Function for downloading the zip file
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )

    # Function for retaining only those files which are .jpeg and are in folder cats or dogs
    def _get_updated_list_of_files(self, list_of_files):
        return [f for f in list_of_files if f.endswith(".jpg") and ("Cat" in f or "Dog" in f)]

    # Function for extracting images one by one if image doesn't exist and if its size is not zero 
    def _preprocess(self, zf: ZipFile, f: str, working_dir: str):
        target_filepath = os.path.join(working_dir, f)
        if not os.path.exists(target_filepath):
            zf.extract(f, working_dir)
        
        if os.path.getsize(target_filepath) == 0:
            os.remove(target_filepath)

    # Reading one by one images from zip and sending it for extraction
    def unzip_and_clean(self):
        with ZipFile(file=self.config.local_data_file, mode="r") as zf:
            list_of_files = zf.namelist(    )
            updated_list_of_files = self._get_updated_list_of_files(list_of_files)
            for f in updated_list_of_files:
                self._preprocess(zf, f, self.config.unzip_dir)