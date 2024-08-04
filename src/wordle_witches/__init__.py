from fastapi import FastAPI
from .server import Server

app = FastAPI()
Server(app)
