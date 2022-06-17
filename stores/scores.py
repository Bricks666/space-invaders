from typing import Dict, Optional
from database import DB
from packages.inject import Inject, Injectable


@Injectable()
@Inject(DB, "__db__")
class ScoresStore:
    __max_scores__: int
    __value__: int
    __level_id__: Optional[int]
    __db__: DB
    __injected__: Dict

    def __init__(self) -> None:
        self.__max_scores__ = 0
        self.__value__ = 0
        self.__level_id__ = None
        self.__db__ = self.__injected__.get("__db__")

    def fetch_max_scores(self, level_id: int) -> None:
        self.__level_id__ = level_id
        max_scores = self.__db__.scores_table.get_best_score(level_id)
        if len(max_scores):
            self.__max_scores__ = max_scores[0].score

    def save_score(self) -> None:
        if self.__level_id__:
            self.__db__.scores_table.add_score(
                self.__level_id__, self.__value__)

    def add(self, value: int) -> None:
        self.__value__ += value

    def get_scores(self) -> int:
        return self.__value__

    def get_max_scores(self) -> int:
        return self.__max_scores__

    def reset_score(self) -> None:
        self.__max_scores__ = max(self.__max_scores__, self.__value__)
        self.__value__ = 0
