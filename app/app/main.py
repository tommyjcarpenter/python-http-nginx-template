#!/usr/bin/env python
from myapi import get_module_logger
from myapi import controller
from myapi import app


if __name__ == "__main__":
    # Entrypoint when testing locally. UWSGI DOES NOT ENTER HERE
    logger = get_module_logger("main")
    logger.debug("Starting locally in development mode")
    app.run(host='0.0.0.0', debug=True, port=10000)
else:
    # Entrypoint in UWSGI
    logger = get_module_logger("main", True)
    controller.logger = get_module_logger("controller", True)
    logger.debug("Starting Application in UWSGI")
