from typing import Dict
from database.db import DB
from packages.inject import Inject, Injectable


@Injectable()
@Inject(DB, "__db__")
class LivesStore:
    __lives__: int
    __injected__: Dict
    __db__: DB

    def __init__(self) -> None:
        self.__lives__ = 0

        self.__db__ = self.__injected__.get("__db__")

    def fetch_lives(self, level_id: int) -> None:
        self.__lives__ = self.__db__.levels_table.get_lives_on_level(level_id)

    def get_lives(self) -> int:
        return self.__lives__

    def decrement_lives(self) -> None:
        self.__lives__ -= 1

    def reset(self) -> None:
        self.__lives__ = 0
