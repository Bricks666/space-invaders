from abc import ABC, abstractmethod
from typing import Final, Generic, List, Optional, Tuple, TypeVar
import sqlite3

R = TypeVar("R", bound=Optional[object])
T = TypeVar("T", bound=Tuple)


class Table(Generic[T, R], ABC):
    """
    Базовый класс для таблицы БД
    """
    __name__: Final[str]
    """
    Имя таблицы
    """

    def __init__(self, connection: sqlite3.Connection, fields: str, name: str):
        self.__name__ = name
        self.__connection__ = connection
        initSQL = f"CREATE TABLE IF NOT EXISTS {self.__name__}(" + \
            fields + ");"
        self.__transaction__(initSQL)

    def __transaction__(self, sql: str) -> List[R]:
        """
        Единый метод для выполнения запросов в БД
        """
        cursor = self.__connection__.cursor()
        cursor.execute(sql)
        response = cursor.fetchall()
        """
        Если был SELECT запрос, то будет возвращен результат
        """
        self.__connection__.commit()
        """
        Если запрос имел иной тип, то требуется сохранить изменения
        """
        return [self.__converter__(data) for data in response]

    @abstractmethod
    def __converter__(self, data: T) -> R:
        """
        Преобразователь данных из БД в ожидаемые данные

        Так как из базы возвращается массив кортежей, а ожидается массив объектов
        """
        pass
