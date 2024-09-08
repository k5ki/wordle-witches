from typing import Dict, List, Self
from wordle_witches.domain.game import Result

from wordle_witches.domain.witch import ColumnCompareResult, Witch

from dataclasses import dataclass


@dataclass
class ChallengeHistory:
    result: Result
    selected_witch: Witch
    column_statuses: Dict[str, ColumnCompareResult]

    def is_already_over(self) -> bool:
        return self.result == Result.ALREADY_OVER


@dataclass
class Player:
    id: str
    challenges: List[ChallengeHistory]

    def challenge_count(self) -> int:
        return len(self.challenges)

    def last_challenge(self) -> ChallengeHistory:
        return self.challenges[-1]

    def append_challenge(self, challenge: ChallengeHistory) -> Self:
        self.challenges.append(challenge)
        return self
