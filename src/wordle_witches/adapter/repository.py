from botocore.tokens import dateutil
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
                team=item["team"],
                birthday=item["birthday"],
                image=item["image"],
            )
            for item in res["Items"]
        ]

    def find_by_id(self, id: int) -> Witch:
        table = self.__db.Table("witches")
        res = table.get_item(Key={"id": id})
        if not res.keys().__contains__("Item"):
            raise Exception(f"Witch (id={id})not found")
        item = res["Item"]
        return Witch(
            id=int(item["id"]),
            name=item["name"],
            nation=item["nation"],
            branch=item["branch"],
            unit=item["unit"],
            team=item["team"],
            birthday=item["birthday"],
            image=item["image"],
        )

    def bingo_witch(self) -> Witch:
        table = self.__db.Table("bingo_witches")
        res = table.scan()  # TODO: フルスキャンせずに最新のレコードを直接取得したい
        items = res["Items"]
        if len(items) == 0:
            raise Exception("No bingo witches")
        items.sort(key=lambda x: x["id"], reverse=True)
        return self.find_by_id(int(items[0]["id"]))
