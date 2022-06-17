
from typing import Final, Tuple


SPRITE_SIZE: Final[int] = 64
BULLET_SIZE: Final[Tuple[int, int]] = (
    SPRITE_SIZE / 100 * 7, SPRITE_SIZE / 100 * 52)

LEVEL_WIDTH: Final[int] = 12 * SPRITE_SIZE
LEVEL_HEIGHT: Final[int] = 14 * SPRITE_SIZE

SCREEN_MARGIN: Final[int] = 50
ASIDE_BAR_WIDTH: Final[int] = SPRITE_SIZE * 5 + 12

WIDTH: Final[int] = LEVEL_WIDTH + ASIDE_BAR_WIDTH + SCREEN_MARGIN * 2
HEIGHT: Final[int] = LEVEL_HEIGHT + SCREEN_MARGIN * 2
BORDER_WIDTH: Final[int] = 5
