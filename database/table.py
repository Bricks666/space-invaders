from abc import ABCMeta, abstractmethod
from typing import List, Optional, Tuple, TypeVar
import sqlite3

R = TypeVar("R", bound=Optional[object])
T = TypeVar("T", bound=Tuple)


class Table(metaclass=ABCMeta):
    __name__: str

    def __init__(self, connection: sqlite3.Connection, fields: str, name: str):
        self.__name__ = name
        self.__connection__ = connection
        initSQL = f"CREATE TABLE IF NOT EXISTS {self.__name__}(" + fields + ");"
        self._transaction_(initSQL)

    def _transaction_(self, sql: str) -> List[R]:
        cursor = self.__connection__.cursor()
        cursor.execute(sql)
        response = cursor.fetchall()
        self.__connection__.commit()
        return [self.__converter__(data) for data in response]

    @abstractmethod
    def __converter__(self, data: T) -> R:
        pass
