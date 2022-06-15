import sqlite3
from typing import List, Tuple
from database.table import Table


class LevelModel:
    level_id: int
    level_name: str
    level_path: str
    lives: int

    def __init__(self, level_id: int, level_name: str, level_path: str, lives: int) -> None:
        self.level_id = level_id
        self.level_name = level_name
        self.level_path = level_path
        self.lives = lives


TableLevel = Tuple[int, str, str, str]


class LevelsTable(Table):
    def __init__(self, connection: sqlite3.Connection) -> None:
        fields = ("level_id INTEGER PRIMARY KEY," +
                  "level_name TEXT NOT NULL," +
                  "level_path TEXT NOT NULL," +
                  "lives INTEGER UNSIGNED")
        super().__init__(connection, fields, "Levels")

    def get_levels(self) -> List[LevelModel]:
        sql = f"SELECT * FROM {self.__name__};"

        return self._transaction_(sql)

    def get_lives_on_level(self, level_id: int):
        pass

    def __converter__(self, data: TableLevel) -> LevelModel:
        return LevelModel(data[0], data[1], data[2], data[3])
