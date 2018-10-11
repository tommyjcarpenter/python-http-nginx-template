#!/usr/bin/env python
import connexion
from myapi import get_module_logger

_logger = get_module_logger(__name__)

app = connexion.App(__name__, specification_dir='.')
app.add_api('swagger.yaml', arguments={'title': 'My API'})

_logger.debug("Starting Application")

if __name__ == "__main__":
    # Entrypoint when testing locally. UWSGI DOES NOT ENTER HERE
    app.run(host='0.0.0.0', debug=True, port=10000)
