from models.response import Response


def response(status, code, data, error=None) -> Response:
    return Response(status=status, code=code, data=data, error=error)
