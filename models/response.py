from pydantic import BaseModel
from typing import Union, Any


class Response(BaseModel):
    status: bool = True
    code: int = 200
    data: Union[None, Any] = None
    error: Union[None, str] = None

    def dict(self, *args, **kwargs):
        # Exclude 'error' field from the response if it is None
        if self.error is None:
            kwargs['exclude'] = {'error'}
        return super().dict(*args, **kwargs)
