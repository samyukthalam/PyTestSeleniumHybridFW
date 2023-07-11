import configparser
import os
from pathlib import Path


def readvaluefrompropfile(valueSection, value):
    config = configparser.RawConfigParser()
    dir1 = Path(__file__)
    dir2=dir1.parent
    dir3=dir2.parent
    prop_file_path = os.path.join(dir3, 'GlobalParameters.properties')
    config.read(prop_file_path)
    return config.get(valueSection, value)


class ReadPropFile:
    pass

