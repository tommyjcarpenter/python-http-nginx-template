#!/usr/bin/env python

import connexion
from myapi import get_module_logger
import os

_logger = get_module_logger(__name__)

app = connexion.App(__name__, specification_dir='.')
app.add_api('swagger.yaml', arguments={'title': 'My API'})


def runapp():
    """Entrypoint when testing locally"""
    try:
        runport = os.environ.get("LISTENPORT", 10000)
        _logger.info("Launching application on port %d", runport)
        app.run(host='0.0.0.0', debug=True, port=runport)
    except Exception as exc:
        _logger.error("Fatal error. Could not start webserver due to: %s", exc)


if __name__ == "__main__":
    # Entrypoint When in uwsgi
    runapp()
