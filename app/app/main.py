#!/usr/bin/env python
from myapi import get_module_logger
from myapi import controller
from myapi import app


_logger = get_module_logger(__name__)


if __name__ == "__main__":
    # Entrypoint when testing locally. UWSGI DOES NOT ENTER HERE
    app.run(host='0.0.0.0', debug=True, port=10000)
else:
    # Entrypoint in UWSGI
    _logger.debug("Setting up file based logging")
    controller.logger = get_module_logger("controller")
    _logger.debug("Starting Application in UWSGI")
