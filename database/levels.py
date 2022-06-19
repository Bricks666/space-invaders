import sqlite3
from typing import List, Optional, Tuple
from .table import Table
from models import LevelModel


TableLevel = Tuple[int, str, str, str]
"""
Кортеж, возвращаемый из БД
"""


class LevelsTable(Table[TableLevel, LevelModel]):
    """
    Таблица уровней
    """

    def __init__(self, connection: sqlite3.Connection) -> None:
        fields = ("level_id INTEGER PRIMARY KEY," +
                  "level_name TEXT NOT NULL," +
                  "level_path TEXT NOT NULL," +
                  "lives INTEGER UNSIGNED")
        super().__init__(connection, fields, "Levels")

    def get_levels(self) -> List[LevelModel]:
        """
        Метод для получение всех уровней из БД
        """
        sql = f"SELECT * FROM {self.__name__};"

        return self.__transaction__(sql)

    def get_lives_on_level(self, level_id: int) -> Optional[int]:
        """
        Метод для получения количества жизней на уровне
        """
        sql = f"SELECT * FROM {self.__name__} WHERE level_id = {level_id} LIMIT 1;"

        level = self.__transaction__(sql)

        if not level:
            return

        return level[0].lives

    def __converter__(self, data: TableLevel) -> LevelModel:
        return LevelModel(data[0], data[1], data[2], data[3])
