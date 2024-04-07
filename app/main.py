from fastapi import FastAPI

from contextlib import asynccontextmanager

from .config import get_config
from .entrypoint import CleanUp, clean_text

global_stores = {}
headers = {"content-type": "application/json"}


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the config
    cfg = get_config()
    global_stores["cfg"] = cfg
    yield
    # Clean up the clients and release the resources
    global_stores.clear()


app = FastAPI(lifespan=lifespan)


@app.post("/")
async def root(body: CleanUp):
    return clean_text(
        CleanUp.parse_obj(body)
    )


@app.get("/healz")
async def healz():
    return {"message": "OK"}


@app.get("/ready")
async def ready():
    return {"message": "Ready"}
