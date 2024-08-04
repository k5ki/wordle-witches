from ..domain.repository import Repository
from ..domain.witch import Witch


class RepositoryImpl(Repository):
    def all(self) -> list[Witch]:
        return [Witch("Hermione"), Witch("Ginny"), Witch("Luna")]
