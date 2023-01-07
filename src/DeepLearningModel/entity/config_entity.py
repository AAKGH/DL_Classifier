from collections import namedtuple
import os

# Defining the entity(Structure) for Data Ingestion Config Object which will serve as input to Data Ingestion Component

DataIngestionConfig = namedtuple("DataIngestionConfig", [
    "root_dir",
    "source_URL",
    "local_data_file",
    "unzip_dir"
])