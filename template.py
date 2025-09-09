import os
from pathlib import Path
import logging # we need logging to print progress in creating files 

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(message)s',
    datefmt='%H:%M:%S'
)

project_name = "cnnChickenDiseaseClassifier" 

list_of_files = [
    ".github/workflows/.gitkeep", # placeholder so GitHub Actions CI/CD workflow folder exists.
    f"src/{project_name}/__init__.py", # init creates a constructor file. makes cnnChickenDiseaseClassifier a Python package.
    f"src/{project_name}/components/__init__.py", #another constructer file for components. package for modules like data ingestion, training, evaluation.
    f"src/{project_name}/utils/__init__.py", # package for helper functions (logging, exception handling, etc.).
    f"src/{project_name}/config/__init__.py", 
    f"src/{project_name}/config/configuration.py", #config manager to load from config.yaml.
    f"src/{project_name}/pipeline/__init__.py", # pipeline scripts (training_pipeline.py, prediction_pipeline.py).
    f"src/{project_name}/entity/__init__.py", # dataclasses (entities for configs/params).
    f"src/{project_name}/constants/__init__.py", # constants (e.g., file paths, schema keys)
    "config/config.yaml", # project settings (data paths, model params).
    "dvc.yaml", # for DVC: the MLOps tool. defines pipeline stages
    "params.yaml", # hyperparameters for training.
    "requirements.txt", # Python dependencies.
    "setup.py", # makes project installable as a package (pip install -e .).
    "research/trials.ipynb", # we need this to perform some notebook experiments before implementing the actual components
]

for filepath in list_of_files:
    filepath = Path(filepath) # because we used forward slash / for file names, but windows OS uses back slashes \ so this avoids errors
    filedir, filename = os.path.split(filepath)

    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # if that file doesnt exist or exists but is empty, create it
        with open(filepath, "w"):
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists and is not empty") # the file path exists already and it's NOT EMPTY
