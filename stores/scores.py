from typing import Optional
from database import DB
from packages.inject import Injector


@Injector.injectable()
@Injector.inject(DB, "__db__")
class ScoresStore:
    """
    Хранилище данных об очках
    """
    __max_scores__: int
    """
    Максимальное количество очков на уровне
    """
    __scores__: int
    """
    Текущее количество очков на уровне
    """
    __level_id__: Optional[int]
    """
    Текущий уровень, нужно для удобства сохранения результатов
    и обеспечения надежности сохранения результатов
    """
    __db__: DB
    """
    БД
    """

    def __init__(self) -> None:
        self.__max_scores__ = 0
        self.__scores__ = 0

    def fetch_max_scores(self, level_id: int) -> None:
        """
        Получения наибольшего количества очков по текущему уровню
        """
        self.__level_id__ = level_id
        max_scores = self.__db__.scores_table.get_best_score(level_id)
        if len(max_scores):
            """
            Возможно, что вернется пустой массив,
            так как БД может быть свежей или в ней не будет данных по текущему уровню
            """
            self.__max_scores__ = max_scores[0].score

        self.__scores__ = 0

    def save(self) -> None:
        """
        Сохранение результатов в БД
        """
        if self.__level_id__:
            """
            Так как возможен вызов метода до выбора уровня
            """
            self.__db__.scores_table.add_score(
                self.__level_id__, self.__scores__)

    def add(self, value: int) -> None:
        """
        Добавления очков
        """
        self.__scores__ += value

    def get_scores(self) -> int:
        """
        Получение очков
        """
        return self.__scores__

    def get_max_scores(self) -> int:
        """
        Получение максимального количества очков
        """
        return self.__max_scores__

    def reset(self) -> None:
        """
        Сброс состояния
        """
        self.__max_scores__ = max(self.__max_scores__, self.__scores__)
        self.__scores__ = 0
