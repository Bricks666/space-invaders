from typing import Final


class ScoreModel:
    """
    Модель, описывающая очки в игре
    """
    score_id: Final[int]
    """
    Id записи об очках
    """
    level_id: Final[int]
    """
    Id уровня
    """
    score: Final[int]
    """
    Количество очков
    """

    def __init__(self, score_id: int, level_id: int, score: int) -> None:
        self.score_id = score_id
        self.level_id = level_id
        self.score = score
