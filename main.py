from pathlib import Path

from fastapi import FastAPI, APIRouter, Request, Depends
from fastapi.staticfiles import StaticFiles

import uvicorn

from app.routers.api import api_router

root_router = APIRouter()
app = FastAPI(title="Binit API")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")


@root_router.get("/", status_code=200)
def root() -> dict:
    return {
        "success": True,
        "code": 200
    }


app.include_router(api_router)
app.include_router(root_router)


if __name__ == "__main__":
    # For debugging purposes only
    print("DEBUG")
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
