from pydantic import BaseModel


class Response(BaseModel):
    status: bool = True
    code: int = 200
    data: any = None
    error: str = None
