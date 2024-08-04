from .witch import Witch
from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def all(self) -> list[Witch]:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> Witch:
        pass

    @abstractmethod
    def bingo_witch(self) -> Witch:
        pass
