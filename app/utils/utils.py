from app.models.response import Response


def response(status, code, data, error=None) -> Response:
    return Response(status, code, data)
