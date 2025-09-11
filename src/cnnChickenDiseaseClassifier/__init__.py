# __init__.py makes a folder (cnnChickenDiseaseClassifier) a python package, so we can import cnnChickenDiseaseClassifier
# here, we'll also use it to set up global logging. that way, we can import logger anywhere in the project and get a consistent logging format
import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log") # creates a folder logs/ if it doesnt exist, and prepares the path for saving logs: logs/running_logs.log.
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[ # send logs both to:
        logging.FileHandler(log_filepath), # a file running_logs
        logging.StreamHandler(sys.stdout) # and the console "stdout"
    ]
)

logger = logging.getLogger("cnnClassifierLogger") # creates a named logger that we can import and use anywhere in project
