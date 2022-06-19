import sqlite3
from typing import Final, Tuple
from .levels import LevelsTable
from .table import Table
from models import ScoreModel


TableScore = Tuple[int, int, int]
"""
Кортеж, возвращаемый из БД
"""


class ScoresTable(Table[TableScore, ScoreModel]):
    """
    Талица очков на уровнях
    """

    def __init__(self, connection: sqlite3.Connection):
        fields = ("score_id INTEGER PRIMARY KEY AUTOINCREMENT," +
                  "level_id INTEGER UNSIGNED," +
                  "score INTEGER UNSIGNED," +
                  f"FOREIGN KEY(level_id) REFERENCES {LevelsTable.__name__}(level_id)")
        super().__init__(connection, fields, "Scores")

    def get_best_score(self, level_id: int):
        """
        Метод для получения максимального количества очков, полученных на уровне
        """
        sql = (f"SELECT * FROM {self.__name__} " +
               f"WHERE level_id = {level_id} " +
               "ORDER BY score DESC LIMIT 1")
        return self.__transaction__(sql)

    def add_score(self, level_id: int, score: int) -> None:
        """
        Метод для добавления записи о полученных очках на уровне
        """
        sql = (f"INSERT INTO {self.__name__}(level_id, score) " +
               f"VALUES({level_id},{score})")
        self.__transaction__(sql)

    def __converter__(self, data: TableScore) -> ScoreModel:
        return ScoreModel(data[0], data[1], data[2])
