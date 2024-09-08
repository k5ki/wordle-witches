from dataclasses import dataclass
from enum import Enum
from typing import Dict, Self


class ColumnCompareResult(Enum):
    MATCHED = "matched"
    PARTIALY_MATCHED = "partialy_matched"
    UNMATCHED = "unmatched"


@dataclass
class Witch:
    id: int
    name: str
    nation: str
    branch: str
    unit: str
    team: str
    birthday: str
    image: str

    def to_dict(self) -> Dict[str, str]:
        return self.__dict__

    def compare(self, witch: Self) -> Dict[str, ColumnCompareResult]:
        return {
            "nation": self.compare_nation(witch.nation),
            "branch": self.compare_branch(witch.branch),
            "unit": self.compare_unit(witch.unit),
            "team": self.compare_team(witch.team),
        }

    def compare_nation(self, nation: str) -> ColumnCompareResult:
        if self.nation == "" or nation == "":
            return ColumnCompareResult.UNMATCHED
        elif self.nation == nation:
            return ColumnCompareResult.MATCHED
        else:
            return ColumnCompareResult.UNMATCHED

    def compare_branch(self, branch: str) -> ColumnCompareResult:
        if self.branch == "" or branch == "":
            return ColumnCompareResult.UNMATCHED
        elif self.branch == branch:
            return ColumnCompareResult.MATCHED
        else:
            return ColumnCompareResult.UNMATCHED

    def compare_unit(self, unit: str) -> ColumnCompareResult:
        if self.unit == "" or unit == "":
            return ColumnCompareResult.UNMATCHED
        elif self.unit == unit:
            return ColumnCompareResult.MATCHED
        else:
            return ColumnCompareResult.UNMATCHED

    def compare_team(self, team: str) -> ColumnCompareResult:
        if self.team == "" or team == "":
            return ColumnCompareResult.UNMATCHED
        elif self.team == team:
            return ColumnCompareResult.MATCHED
        else:
            return ColumnCompareResult.UNMATCHED
