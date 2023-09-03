from app.models.response import Response


def response(status, code, data, error=None) -> Response:
    return Response(status, code, data)


def is_garbage_type(type: str) -> bool:
    types = ['Yard Waste', 'HHW', 'Electronic Waste',
             'Garbage', 'Organic', 'Recycle']

    return type in types
