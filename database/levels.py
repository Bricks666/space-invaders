import sqlite3
from typing import Final, List, Optional, Tuple
from database.table import Table


class LevelModel:
    level_id: Final[int]
    level_name: Final[str]
    level_path: Final[str]
    lives: Final[int]

    def __init__(self, level_id: int, level_name: str, level_path: str, lives: int) -> None:
        self.level_id = level_id
        self.level_name = level_name
        self.level_path = level_path
        self.lives = lives


TableLevel = Tuple[int, str, str, str]


class LevelsTable(Table[TableLevel, LevelModel]):
    def __init__(self, connection: sqlite3.Connection) -> None:
        fields = ("level_id INTEGER PRIMARY KEY," +
                  "level_name TEXT NOT NULL," +
                  "level_path TEXT NOT NULL," +
                  "lives INTEGER UNSIGNED")
        super().__init__(connection, fields, "Levels")

    def get_levels(self) -> List[LevelModel]:
        sql = f"SELECT * FROM {self.__name__};"

        return self._transaction_(sql)

    def get_lives_on_level(self, level_id: int) -> Optional[int]:
        sql = f"SELECT * FROM {self.__name__} WHERE level_id = {level_id} LIMIT 1;"

        level = self._transaction_(sql)

        if not level:
            return

        return level[0].lives

    def __converter__(self, data: TableLevel) -> LevelModel:
        return LevelModel(data[0], data[1], data[2], data[3])
