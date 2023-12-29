import logging


# class LogGen:
#     @staticmethod
#     def loggen():
#         logging.basicConfig(filename='.\\Logs\\automation.log', format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p', level=logging.DEBUG, force=True)
#         logger = logging.getLogger()
#         logger.setLevel(logging.INFO)
#         return logger


import logging
import os
import sys

cwd = os.getcwd()
sys.path.append(cwd)
# sys.path.append(cwd + "/automation/")

# configure logging with filename, function name and line numbers
logging.basicConfig(
    filename='.\\Logs\\automation.log',
    level="INFO",
    datefmt="%I:%M:%S %p %Z",
    format="%(levelname)s [%(asctime)s - %(filename)s:%(lineno)s::%(funcName)s]\n%(message)s",
    force=True
)

log = logging.getLogger(__name__)
