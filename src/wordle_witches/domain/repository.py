from wordle_witches.domain.player import Player
from .witch import Witch
from abc import ABC, abstractmethod


class WitchRepository(ABC):
    @abstractmethod
    def all(self) -> list[Witch]:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> Witch:
        pass

    @abstractmethod
    def bingo_witch(self) -> Witch:
        pass


class PlayerRepository(ABC):
    @abstractmethod
    def find_by_id(self, id: str) -> Player:
        pass

    @abstractmethod
    def save(self, player) -> None:
        pass

    @abstractmethod
    def create() -> Player:
        pass

    @abstractmethod
    def reset_data(self, id: str) -> None:
        pass
