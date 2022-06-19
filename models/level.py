from typing import Final


class LevelModel:
    """
    Модель уровня, используемая в игре
    """
    level_id: Final[int]
    """
    Id уровня
    """
    level_name: Final[str]
    """
    Название уровня
    """
    level_path: Final[str]
    """
    Путь до уровня
    """
    lives: Final[int]
    """
    Количество жизней на уровне
    """

    def __init__(self, level_id: int, level_name: str, level_path: str, lives: int) -> None:
        self.level_id = level_id
        self.level_name = level_name
        self.level_path = level_path
        self.lives = lives
