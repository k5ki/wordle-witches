from ..domain.repository import Repository
from ..domain.witch import Witch
import boto3


class RepositoryImpl(Repository):
    def __init__(self, dynamodb) -> None:
        self.__db = dynamodb

    def all(self) -> list[Witch]:
        table = self.__db.Table("witches")
        res = table.scan()
        return [
            Witch(
                id=int(item["id"]),
                name=item["name"],
                nation=item["nation"],
                branch=item["branch"],
                unit=item["unit"],
                birthday=item["birthday"],
                image=item["image"],
            )
            for item in res["Items"]
        ]
