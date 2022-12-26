# The template file contains information about all the filenames that are required in project skeleton

# The template file also contains the code to create the skeleton 

# Importing the libraries required for execution of template file
import os
from pathlib import Path
import logging

# Setting up priority level and format of logging messages
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s: ')

# Defining the name of project model
package_name = "DeepLearningModel"

# Defining the list of files required to be created in project skeleton
list_of_files = [
   ".github/workflows/.gitkeep",
   f"src/{package_name}/__init__.py", 
   f"src/{package_name}/components/__init__.py", 
   f"src/{package_name}/utils/__init__.py", 
   f"src/{package_name}/config/__init__.py", 
   f"src/{package_name}/pipeline/__init__.py", 
   f"src/{package_name}/entity/__init__.py", 
   f"src/{package_name}/constants/__init__.py",
   "tests/__init__.py",
   "tests/unit/__init__.py",
   "tests/integration/__init__.py",
   "configs/config.yaml",
   "dvc.yaml",
   "params.yaml",
   "init_setup.sh",
   "requirements.txt", 
   "requirements_dev.txt",
   "setup.py",
   "setup.cfg",
   "pyproject.toml",
   "tox.ini",
   "research/trials.ipynb", 
]

# Actual creation of project skeleton
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    # Creating folders for files when required
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    # Creating empty files
    if (not os.path.exists(filepath)):
        with open(filepath, "w") as f:
            pass # create an empty file
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")