from fastapi.requests import Request
from wordle_witches.domain.game import Game
from ..domain.repository import Repository


class Controller:
    def __init__(self, repository: Repository) -> None:
        self.repository = repository

    def get_list(self) -> list[dict]:
        return [w.__dict__ for w in self.repository.all()]

    async def post_challenge(self, request: Request) -> dict:
        json = await request.json()
        witch_id = int(json["witch_id"])
        game = Game(self.repository)
        return game.challenge(witch_id).__dict__
