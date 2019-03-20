"""
Module that handles logging
"""
import connexion
import logging
import logging.handlers

# this must go first due to a cyclic loop
def get_module_logger(mod_name, filetoo = False):
    logger = logging.getLogger(mod_name)
    # 100MB log, up to 5
    handler = logging.StreamHandler()
    formatter = logging.Formatter('[%(asctime)-20s] [%(name)-12s] [%(levelname)-8s] %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    if filetoo:
        handler2 = logging.handlers.RotatingFileHandler("/opt/logs/log.txt", maxBytes=100000000, backupCount=5)
        handler2.setFormatter(formatter)
        logger.addHandler(handler2)

    return logger

app = connexion.App(__name__, specification_dir='.')
app.add_api('openapi.yaml', arguments={'title': 'My API'})
