import boto3
from fastapi import FastAPI, Response
from fastapi.requests import Request

from .adapter.controller import Controller
from .adapter.repository import PlayerRepositoryImpl, WitchRepositoryImpl


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
        witch_repository = WitchRepositoryImpl(dynamodb)
        player_repository = PlayerRepositoryImpl(dynamodb)
        self.controller = Controller(witch_repository, player_repository)
        self.__add_routes()

    def __add_routes(self) -> None:
        @self.app.get("/")
        async def root() -> dict:
            return {"message": "Hello World"}

        @self.app.get("/witches")
        async def list_witches() -> list[dict]:
            return self.controller.get_witches()

        @self.app.get("/witches/{id}")
        async def get_witch(id: int) -> dict:
            return self.controller.get_witch(id)

        @self.app.post("/challenge")
        async def challenge(request: Request, response: Response) -> dict:
            return await self.controller.post_challenge(request, response)

        @self.app.post("/reset")
        async def reset(request: Request, response: Response) -> None:
            return self.controller.reset_session(request, response)
