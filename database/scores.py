import sqlite3
from typing import List, Tuple
from database.table import Table


class Score:
    score: int


class ScoresTable(Table):
    NAME = "Scores"

    def __init__(self, connection: sqlite3.Connection):
        initSQL = (f"CREATE TABLE IF NOT EXISTS {self.NAME}(" +
                   "score INTEGER UNSIGNED);")
        super().__init__(connection, initSQL)

    def get_best_score(self) -> List[Tuple[int]]:
        sql = (f"SELECT * FROM {self.NAME} " + "ORDER BY score DESC LIMIT 1")
        return self._transaction_(sql)

    def add_score(self, score: int):
        sql = (f"INSERT INTO {self.NAME} " +
               f"VALUES({score})")
        self._transaction_(sql)
