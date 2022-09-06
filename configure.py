
import configparser

def setConfiguration():

    db_config = configparser.ConfigParser()
    db_config.read('utils/all_config.cfg')

    return db_config
