from app.models.response import Response


def response(status, code, data, error=None) -> Response:
    return Response(status, code, data)


def is_garbage_type(type: str) -> bool:
    types = ['yard waste', 'hhw', 'electronic waste',
             'garbage', 'organic', 'recycle']

    return type in types
