import connexion
from flask import Response
import logging
from myapi import get_module_logger

# will be set in uwsgi later (main.py sets this)
logger = get_module_logger(__name__)


def foo_handler(bar):
    """demonstration of path parameter, see swagger"""
    logger.debug("foo handler called")
    return Response(response=bar,
                    status=200)


def baz_handler():
    """demonstration of function with post body, see swagger"""
    logger.debug("baz handler called")
    body = connexion.request.json
    query_string = body.get("query_string")
    return Response(response=query_string,
                    status=200)
