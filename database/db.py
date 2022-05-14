import mysql.connector
from mysql.connector import Error

from database.users import UsersTable


class DB:
    def __init__(self, name="Tasks"):
        self.__name = name

    def init(self, login: str, password: str) -> None:
        self.__connection: mysql.connector.MySQLConnection = self.createConnection(
            login, password)
        cursor = self.__connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.__name}")
        self.__connection.database = self.__name
        self.__connection.commit()
        self.users_table = UsersTable(self.__connection)

    def createConnection(self, login: str, password: str) -> mysql.connector.MySQLConnection:
        connection = None
        try:
            connection = mysql.connector.connect(user=login, password=password)
        except Error:
            print("Connection error")

        return connection

    def disconnect(self) -> None:
        self.__connection.close()
        self.__connection = None


db = DB()
