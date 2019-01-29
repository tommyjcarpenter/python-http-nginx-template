"""
Module that handles logging
"""
import connexion
import logging
import logging.handlers


app = connexion.App(__name__, specification_dir='.')
app.add_api('openapi.yaml', arguments={'title': 'My API'})


def get_module_logger(mod_name):
    """
    To use this, do logger = get_module_logger(__name__)
    """
    logger = logging.getLogger(mod_name)
    # 100MB log, up to 5
    handler = logging.handlers.RotatingFileHandler("/opt/logs/log.txt", maxBytes=100000000, backupCount=5)
    handler2 = logging.StreamHandler()
    formatter = logging.Formatter('[%(asctime)-20s] [%(name)-20s] [%(levelname)-8s] %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.addHandler(handler2)
    logger.setLevel(logging.DEBUG)
    return logger
