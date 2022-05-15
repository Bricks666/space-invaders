from typing import Dict, List, TypeVar
import sqlite3

T = TypeVar("T", bound=object | None)


class Table:
    NAME: str

    def __init__(self, connection: sqlite3.Connection, initSQL: str):
        self.__connection__ = connection
        self._transaction_(initSQL)

    def _transaction_(self, sql: str, data: Dict = {}) -> List[T]:
        cursor = self.__connection__.cursor()
        cursor.execute(sql, data)
        response = cursor.fetchall()
        self.__connection__.commit()
        return list(response)
