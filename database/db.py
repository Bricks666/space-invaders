from sqlite3 import connect
import sqlite3
from database.scores import ScoresTable


class DB:
    def __init__(self, name="space-invaders"):
        self.__name__ = name

    def init(self) -> None:
        self.__connection__: sqlite3.Connection = self.__createConnection__()
        self.__connection__.commit()
        self.scores_table = ScoresTable(self.__connection__)

    def __createConnection__(self) -> sqlite3.Connection:
        connection = None
        try:
            connection = connect(database=self.__name__)
        except:
            print("Connection error")

        return connection

    def disconnect(self) -> None:
        self.__connection__.close()
        self.__connection__ = None


db = DB()
