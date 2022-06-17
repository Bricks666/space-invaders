from typing import Final


class ScoreModel:
    score_id: Final[int]
    level_id: Final[int]
    score: Final[int]

    def __init__(self, score_id: int, level_id: int, score: int) -> None:
        self.score_id = score_id
        self.level_id = level_id
        self.score = score
