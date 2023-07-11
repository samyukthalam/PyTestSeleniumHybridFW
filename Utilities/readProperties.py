import configparser
import os
from pathlib import Path

config = configparser.ConfigParser()
configIniFilePath = os.path.join(os.path.sep, Path(__file__).parent.parent, 'Configurations/config.ini')
config.read(configIniFilePath)


class ReadConfigFile:

    @staticmethod
    def getApplicationURL():
        print("Config file path is " + configIniFilePath)
        print(config.sections())
        url = config.get("app url section", "appUrl")
        return url

    @staticmethod
    def getUserName():
        username = config.get("app login section", "userName")
        return username

    @staticmethod
    def getAPassword():
        password = config.get("app login section", "password")
        return password
