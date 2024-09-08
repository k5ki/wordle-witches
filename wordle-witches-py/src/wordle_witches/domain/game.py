from dataclasses import dataclass
from enum import Enum

from wordle_witches.domain.player import ChallengeHistory, Player
from wordle_witches.domain.witch import Witch


class Result(Enum):
    CORRECT = "correct"
    GAME_OVER = "game_over"
    MISS = "miss"
    ALREADY_OVER = "already_over"


@dataclass
class State:
    player: Player


class Game:
    def __init__(self, bingo_witch: Witch) -> None:
        self.bingo_witch = bingo_witch
        self.max_challenge_count = 5

    def challenge(self, state: State, witch: Witch) -> State:
        player = state.player

        result = Result.MISS
        if player.challenge_count() == self.max_challenge_count:
            result = Result.ALREADY_OVER
        elif witch.id == self.bingo_witch.id:
            result = Result.CORRECT
        elif player.challenge_count() == self.max_challenge_count - 1:
            result = Result.GAME_OVER

        player.append_challenge(
            ChallengeHistory(result, witch, self.bingo_witch.compare(witch))
        )
        return State(player)
