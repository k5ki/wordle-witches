from typing_extensions import List
from wordle_witches.domain.player import Guess, Player

from wordle_witches.domain.repository import PlayerRepository, WitchRepository


class Result:
    def __init__(self, result: str, guesses: List[Guess]):
        self.result = result
        self.guesses = guesses


class Game:
    def __init__(
        self,
        player: Player,
        witch_repository: WitchRepository,
        player_repository: PlayerRepository,
    ) -> None:
        self.player = player
        self.witch_repository = witch_repository
        self.player_repository = player_repository

    def challenge(self, witch_id: int) -> Result:
        if self.player.challenge_count() == 5:
            return Result("game over", self.player.guesses)

        expected = self.witch_repository.bingo_witch()
        selected = self.witch_repository.find_by_id(witch_id)
        if expected.id == selected.id:
            self.player.guesses.append(
                Guess(
                    selected.id,
                    ["name", "nation", "branch", "unit", "team", "birthday"],
                )
            )
            return Result("bingo", self.player.guesses)

        hint = []
        if expected.nation == selected.nation and expected.nation != "":
            hint.append("nation")
        if expected.branch == selected.branch and expected.branch != "":
            hint.append("branch")
        if expected.unit == selected.unit and expected.unit != "":
            hint.append("unit")
        if expected.team == selected.team and expected.team != "":
            hint.append("team")
        if expected.birthday == selected.birthday and expected.birthday != "":
            hint.append("birthday")

        self.player.guesses.append(Guess(selected.id, hint))
        self.player_repository.save(self.player)

        if self.player.challenge_count() == 5:
            return Result("game over", self.player.guesses)
        else:
            return Result("miss", self.player.guesses)
