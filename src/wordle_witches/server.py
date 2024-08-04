import boto3
from fastapi import FastAPI
from fastapi.requests import Request

from .adapter.controller import Controller
from .adapter.repository import RepositoryImpl


class Server:
    def __init__(self, app: FastAPI) -> None:
        self.app = app

        dynamodb = boto3.resource(
            service_name="dynamodb",
            endpoint_url="http://localhost:8181",
            region_name="ap-northeast-1",
            aws_access_key_id="AKI000000000000000",
            aws_secret_access_key="secret_access_key",
        )
        repository = RepositoryImpl(dynamodb)
        self.controller = Controller(repository)
        self.__add_routes()

    def __add_routes(self) -> None:
        @self.app.get("/")
        async def root() -> dict:
            return {"message": "Hello World"}

        @self.app.get("/list")
        async def list_witches() -> list[dict]:
            return self.controller.get_list()

        @self.app.post("/challenge")
        async def challenge(request: Request) -> dict:
            return await self.controller.post_challenge(request)
