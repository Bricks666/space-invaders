import sqlite3
from typing import List, Tuple
from database.levels import LevelsTable
from database.table import Table


class ScoreModel:
    score_id: int
    level_id: int
    score: int

    def __init__(self, score_id: int, level_id: int, score: int) -> None:
        self.score_id = score_id
        self.level_id = level_id
        self.score = score


TableScore = Tuple[int, int, int]


class ScoresTable(Table):
    def __init__(self, connection: sqlite3.Connection):
        fields = ("score_id INTEGER UNSIGNED PRIMARY KEY," +
                  "level_id INTEGER UNSIGNED," +
                  "score INTEGER UNSIGNED," +
                  f"FOREIGN KEY(level_id) REFERENCES {LevelsTable.__name__}(level_id)")
        super().__init__(connection, fields, "Scores")

    def get_best_score(self, level_id: int = 1) -> List[Tuple[int]]:
        sql = (f"SELECT * FROM {self.__name__} " +
               f"WHERE level_id = {level_id}" +
               "ORDER BY score DESC LIMIT 1")
        return self._transaction_(sql)

    def add_score(self, level_id: int, score: int) -> None:
        sql = (f"INSERT INTO {self.__name__}(level_id, score) " +
               f"VALUES({level_id},{score})")
        self._transaction_(sql)

    def __converter__(self, data: TableScore) -> ScoreModel:
        return ScoreModel(data[0], data[1], data[2])
