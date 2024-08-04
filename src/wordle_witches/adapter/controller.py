from .repository import RepositoryImpl


class Controller:
    def __init__(self) -> None:
        self.repository = RepositoryImpl()

    def get_list(self) -> list[dict]:
        return [w.__dict__ for w in self.repository.all()]
