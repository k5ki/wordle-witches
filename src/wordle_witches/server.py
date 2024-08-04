from fastapi import FastAPI

from .adapter.controller import Controller


class Server:
    def __init__(self, app: FastAPI) -> None:
        self.app = app
        self.controller = Controller()
        self._add_routes()

    def _add_routes(self) -> None:
        @self.app.get("/")
        async def root() -> dict:
            return {"message": "Hello World"}

        @self.app.get("/list")
        async def list_witches() -> list[dict]:
            return self.controller.get_list()
