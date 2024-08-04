from typing_extensions import List

from wordle_witches.domain.repository import Repository


class GameResult:
    def __init__(self, result: str, hint: List[str] | None):
        self.result = result
        self.hint = hint


class Game:
    def __init__(self, repository: Repository) -> None:
        self.repository = repository

    def challenge(self, witch_id: int) -> GameResult:
        expected = self.repository.bingo_witch()
        selected = self.repository.find_by_id(witch_id)
        if expected.id == selected.id:
            return GameResult("bingo", None)
        hint = []
        if expected.nation == selected.nation:
            hint.append("nation")
        if expected.branch == selected.branch:
            hint.append("branch")
        if expected.unit == selected.unit:
            hint.append("unit")
        if expected.team == selected.team:
            hint.append("team")
        if expected.birthday == selected.birthday:
            hint.append("birthday")

        return GameResult("miss", hint)
