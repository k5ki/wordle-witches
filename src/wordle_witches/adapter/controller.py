from fastapi import Request, Response
from wordle_witches.domain.game import Game
from wordle_witches.domain.player import Player

from ..domain.repository import PlayerRepository, WitchRepository


class Controller:
    def __init__(
        self, witch_repository: WitchRepository, player_repository: PlayerRepository
    ) -> None:
        self.witch_repository = witch_repository
        self.player_repository = player_repository

    def get_list(self) -> list[dict]:
        return [w.__dict__ for w in self.witch_repository.all()]

    async def post_challenge(self, request: Request, response: Response) -> dict:
        player = None
        sid = request.cookies.get("wordle_witches_session_id", None)
        if sid is None:
            player = self.__create_new_player(response)
        else:
            player = self.player_repository.find_by_id(sid)
            if player is None:
                player = self.__create_new_player(response)
        json = await request.json()
        witch_id = int(json["witch_id"])
        game = Game(player, self.witch_repository, self.player_repository)
        result = game.challenge(witch_id)
        return {
            "result": result.result,
            "guesses": [
                {
                    "witch": self.witch_repository.find_by_id(g.witch_id).__dict__,
                    "hint": g.hint,
                }
                for g in result.guesses
            ],
        }

    def __create_new_player(self, response: Response) -> Player:
        player = self.player_repository.create()
        response.set_cookie(key="wordle_witches_session_id", value=player.id)
        return player

    def reset_session(self, request: Request, response: Response) -> None:
        sid = request.cookies.get("wordle_witches_session_id", None)
        if sid is None:
            return None
        self.player_repository.reset_data(sid)
