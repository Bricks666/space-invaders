from enum import Enum
from typing import Final, final


@final
class Direction(Enum):
    LEFT: Final[int] = -1
    RIGHT: Final[int] = 1
    TOP: Final[int] = -1
    BOTTOM: Final[int] = 1


@final
class BulletType(Enum):
    HERO: Final[int] = -1
    ENEMY: Final[int] = 1


FIRE_COOLDOWN: Final[float] = 1

FPS: Final[int] = 60


@final
class Entities(Enum):
    HERO: Final[str] = "0"
    ENEMY: Final[str] = "1"


STEP: Final[int] = 4

UNICODE_NUMBER_OFFSET: Final[int] = 48

GAME_NAME: Final[str] = "Space Invaders"
