from enum import Enum
from typing import Final, final


@final
class BulletType(Enum):
    HERO: Final[int] = -1
    ENEMY: Final[int] = 1


FIRE_COOLDOWN: Final[float] = 1

FPS: Final[int] = 60


@final
class EntityCodes(Enum):
    HERO: Final[str] = "0"
    ENEMY: Final[str] = "1"


STEP: Final[int] = 4

UNICODE_NUMBER_OFFSET: Final[int] = 48

GAME_NAME: Final[str] = "Space Invaders"
"""
Остальные константы игры
"""
