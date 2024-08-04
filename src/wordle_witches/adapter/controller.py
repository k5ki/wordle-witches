from ..domain.repository import Repository


class Controller:
    def __init__(self, repository: Repository) -> None:
        self.repository = repository

    def get_list(self) -> list[dict]:
        return [w.__dict__ for w in self.repository.all()]
