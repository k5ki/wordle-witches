from dataclasses import dataclass
from typing import Self
from fastapi import Request, Response
from wordle_witches.domain.game import Game, State as GameState
from wordle_witches.domain.player import Player

from ..domain.repository import PlayerRepository, WitchRepository


@dataclass
class ChallengeRequest:
    witch_id: int

    @classmethod
    def from_dict(cls, data: dict) -> Self:
        if not hasattr(data, "witch_id"):
            raise Exception("")
        return cls(int(data.get("witch_id")))  # type: ignore


class Controller:
    def __init__(
        self, witch_repository: WitchRepository, player_repository: PlayerRepository
    ) -> None:
        self.witch_repository = witch_repository
        self.player_repository = player_repository

    def get_witches(self) -> list[dict]:
        return [w.to_dict() for w in self.witch_repository.all()]

    def get_witch(self, id: int) -> dict:
        return self.witch_repository.find_by_id(id).to_dict()

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
        req = ChallengeRequest.from_dict(json)

        selected_witch = self.witch_repository.find_by_id(req.witch_id)
        bingo_witch = self.witch_repository.bingo_witch()

        game = Game(bingo_witch)

        state = game.challenge(GameState(player), selected_witch)
        player = state.player

        self.player_repository.save(player)

        return result.to_dict()

    def __create_new_player(self, response: Response) -> Player:
        player = self.player_repository.create()
        response.set_cookie(key="wordle_witches_session_id", value=player.id)
        return player

    def reset_session(self, request: Request, response: Response) -> None:
        sid = request.cookies.get("wordle_witches_session_id", None)
        if sid is None:
            return None
        self.player_repository.reset_data(sid)
