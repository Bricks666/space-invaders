from typing import Dict
from database.db import DB
from packages.inject import Inject, Injectable


@Injectable()
@Inject(DB, "__db__")
class ScoresStore:
    __db__: DB
    __injected__: Dict

    def __init__(self) -> None:
        self.__max_scores__ = 0
        self.__value__ = 0
        self.__db__ = self.__injected__.get("__db__")

    def fetch_max_scores(self, level_id: int) -> None:
        max_scores = self.__db__.scores_table.get_best_score(level_id)
        self.__max_scores__ = max_scores

    def save_score(self) -> None:
        self.__db__.scores_table.add_score(self.__value__)

    def add(self, value: int) -> None:
        self.__value__ += value

    def get_scores(self) -> int:
        return self.__value__

    def get_max_scores(self) -> int:
        return self.__max_scores__

    def reset_score(self) -> None:
        self.__max_scores__ = max(self.__max_scores__, self.__value__)
        self.__value__ = 0
