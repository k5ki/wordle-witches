from botocore.credentials import datetime

from wordle_witches.domain.player import Guess, Player
from ..domain.repository import PlayerRepository, WitchRepository
from ..domain.witch import Witch
import boto3
import uuid


class WitchRepositoryImpl(WitchRepository):
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
            raise Exception(f"Witch(id={id}) not found")
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


class PlayerRepositoryImpl(PlayerRepository):
    def __init__(self, dynamodb) -> None:
        self.__db = dynamodb

    def find_by_id(self, id: str) -> Player | None:
        table = self.__db.Table("players")
        res = table.get_item(Key={"id": id})
        if not res.keys().__contains__("Item"):
            return None
        item = res["Item"]
        return Player(
            id=item["id"],
            guesses=[
                Guess(g.get("witch_id"), g.get("hint")) for g in item["guesses"]
            ],  # NOTE: guesses=item["guesses"] とすると dict で返ってくる
        )

    def save(self, player: Player) -> None:
        table = self.__db.Table("players")
        table.put_item(
            Item={
                "id": player.id,
                "guesses": [g.__dict__ for g in player.guesses],
                "created_at": datetime.date.today().isoformat(),
            }
        )

    def create(self) -> Player:
        sid = str(uuid.uuid4())
        player = Player(id=sid, guesses=[])
        self.save(player)  # TDOO: 例外処理 ID衝突可能性
        return player

    def reset_data(self, id: str) -> None:
        table = self.__db.Table("players")
        table.delete_item(Key={"id": id})
        table.put_item(Item={"id": id, "guesses": []})
