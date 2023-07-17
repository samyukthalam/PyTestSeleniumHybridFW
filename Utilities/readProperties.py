import configparser
import os
from pathlib import Path

config = configparser.ConfigParser()
configIniFilePath = os.path.join(os.path.sep, Path(__file__).parent.parent, 'Configurations/config.ini')
config.read(configIniFilePath)


class ReadConfigFile:

    @staticmethod
    def getApplicationURL(section):
        print("Config file path is " + configIniFilePath)
        print(config.sections())
        url = config.get(section, "appUrl")
        return url

    @staticmethod
    def getUserName(section):
        username = config.get(section, "userName")
        return username

    @staticmethod
    def getAPassword(section):
        password = config.get(section, "password")
        return password
