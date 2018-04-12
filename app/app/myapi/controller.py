import connexion
from flask import Response


def foo_handler(bar):
    """demonstration of path parameter, see swagger"""
    return Response(response=bar,
                    status=200)


def baz_handler():
    """demonstration of function with post body, see swagger"""
    body = connexion.request.json
    query_string = body.get("query_string")
    return Response(response=query_string,
                    status=200)
