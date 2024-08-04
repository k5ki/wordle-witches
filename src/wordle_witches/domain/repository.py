from .witch import Witch
from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def all(self) -> list[Witch]:
        pass
