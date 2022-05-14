from typing import Any, List, TypeVar
import sqlite3

T = TypeVar("T", bound=object | None)

class Table:
    NAME: str
    def __init__(self, connection: sqlite3.Connection, initSQL: str):
        self.__connection = connection
        self._transaction(initSQL)
    def _transaction(self, sql:str, **kwargs) -> List[T]:
        cursor = self.__connection.cursor()
        cursor.execute(sql, kwargs.get("data"))
        response = cursor.fetchall()
        self.__connection.commit()
        return list(response)
