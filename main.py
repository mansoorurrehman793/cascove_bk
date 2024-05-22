from typing import Union

from fastapi import FastAPI, Body
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field
from typing_extensions import Annotated
import requests
import uvicorn


app = FastAPI()


@app.get("/")  # decoraters
def read():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
