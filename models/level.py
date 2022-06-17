from typing import Final


class LevelModel:
    level_id: Final[int]
    level_name: Final[str]
    level_path: Final[str]
    lives: Final[int]

    def __init__(self, level_id: int, level_name: str, level_path: str, lives: int) -> None:
        self.level_id = level_id
        self.level_name = level_name
        self.level_path = level_path
        self.lives = lives
