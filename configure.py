
import configparser

def setConfiguration():
    '''
    Returns a dictionary with the DBconfig, Regex objects and TC pipeline
    '''
    db_config = configparser.ConfigParser()
    db_config.read('utils/all_config.cfg')

    return db_config
