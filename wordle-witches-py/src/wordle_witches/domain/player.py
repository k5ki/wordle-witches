from typing import List
from enum import Enum
from wordle_witches.domain.player import Guess

from wordle_witches.domain.witch import Witch


class ChallengeStatus(Enum):
    CORRECT = 1
    GAME_OVER = 2
    MISS = 3


class ColumnStatus(Enum):
    MATCHED = 1
    PARTIALY_MATCHED = 2
    UNMATCHED = 3


class ChallengeHistory:
    def __init__(self, witch: Witch, column_statuses: List[ColumnStatus]) -> None:
        self.witch = witch
        self.column_statuses = column_statuses


class Player:
    def __init__(self, id: str, guesses: list[Guess]):
        self.id = id
        self.guesses = guesses

    def challenge_count(self) -> int:
        return len(self.guesses)
