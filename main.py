from fastapi import FastAPI, Body
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field
from typing_extensions import Annotated
import requests


app = FastAPI()


@app.get("/")  # decoraters
def read():
    return {"Hello": "World"}

