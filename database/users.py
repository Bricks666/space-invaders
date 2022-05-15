from typing import List
import mysql.connector

from database.table import Table


class InsertUserModel:
    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password


class UserModel(InsertUserModel):
    def __init__(self, userId: int, login: str, password: str):
        super().__init__(login, password)
        self.userId = userId


class UsersTable(Table):
    NAME = "users"

    def __init__(self, connection: mysql.connector.MySQLConnection):
        initSQL = (f"CREATE TABLE IF NOT EXISTS {self.NAME}(" +
                   "userId SMALLINT UNSIGNED PRIMARY KEY AUTO_INCREMENT ," +
                   "login VARCHAR(32) NOT NULL," +
                   "password VARCHAR(128) NOT NULL)")
        super().__init__(connection, initSQL)

    def insert_user(self, user: InsertUserModel) -> None:
        sql = (f"INSERT INTO {self.NAME}"+
             "(login, password)", "VALUES"+
             "(%(login)s, %(password)s)")
        self._transaction_(sql, data=user)

    def get_user(self, login: str, password: str) -> List[UserModel]:
        sql= (
            f"SELECT * FROM {self.NAME} " +
            f"WHERE login = '{login}' AND password = '{password}'"
        )

        return self._transaction_(sql)
