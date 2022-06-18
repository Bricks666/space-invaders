from sqlite3 import connect
import sqlite3
from typing import Optional
from database.levels import LevelsTable
from database.scores import ScoresTable
from packages.inject import Injector


@Injector.injectable()
class DB:
    def __init__(self, name="space-invaders") -> None:
        self.__name__ = name

    def init(self) -> None:
        self.__connection__: sqlite3.Connection = self.__createConnection__()
        if not self.__connection__:
            raise Exception("Connection wasn't created")
        self.levels_table = LevelsTable(self.__connection__)
        self.scores_table = ScoresTable(self.__connection__)
        self.__connection__.commit()

    def __createConnection__(self) -> Optional[sqlite3.Connection]:
        connection = None
        try:
            connection = connect(database=self.__name__)
        except:
            print("Connection error")

        return connection

    def disconnect(self) -> None:
        self.__connection__.close()
        self.__connection__ = None
