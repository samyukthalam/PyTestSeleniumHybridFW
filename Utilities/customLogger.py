import logging
import os
import sys
from pathlib import Path
import logging.config

class LogGen:

    @staticmethod
    def logGen():
        logConfFilePath = os.path.join(os.path.sep, Path(__file__).parent.parent, 'Configurations/logging.conf')
        logging.config.fileConfig(logConfFilePath)
        logger = logging.getLogger()
        # logFilePath = os.path.join(os.path.sep, Path(__file__).parent.parent, 'Logs/automation.log')
        # logging.basicConfig(filename = logFilePath)
        # logger.addHandler(logging.FileHandler(logFilePath))
        # logger.addHandler(logging.StreamHandler(stream=sys.stdout))
        # logger.setLevel(logging.INFO)
        return logger