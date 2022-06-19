from sqlite3 import connect
import sqlite3
from typing import Optional
from .levels import LevelsTable
from .scores import ScoresTable
from packages.inject import Injector


@Injector.injectable()
class DB:
    """
    База данных
    """

    levels_table: LevelsTable
    """
    Таблица с уровнями
    """
    scores_table: ScoresTable
    """
    Таблица очков
    """
    __name__: str
    """
    Название БД
    """
    __connection__: sqlite3.Connection
    """
    Соединение с БД
    """

    def __init__(self, name="space-invaders") -> None:
        self.__name__ = name

    def init(self) -> None:
        """
        Метод для соединения с БД и созданием таблиц в ней
        """
        self.__connection__: sqlite3.Connection = self.__createConnection__()
        if not self.__connection__:
            raise Exception("Connection wasn't created")
        self.levels_table = LevelsTable(self.__connection__)
        self.scores_table = ScoresTable(self.__connection__)
        self.__connection__.commit()

    def __createConnection__(self) -> Optional[sqlite3.Connection]:
        """
        Создание соединения с БД
        """
        connection = None
        try:
            connection = connect(database=self.__name__)
        except:
            print("Connection error")

        return connection

    def disconnect(self) -> None:
        """
        Отключение от БД
        """
        self.__connection__.close()
        self.__connection__ = None
