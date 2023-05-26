from typing import Final


SPRITE_SIZE: Final[int] = 64

ROW_COUNT: Final[int] = 12
COLUMN_COUNT: Final[int] = 14

LEVEL_WIDTH: Final[int] = ROW_COUNT * SPRITE_SIZE
LEVEL_HEIGHT: Final[int] = COLUMN_COUNT * SPRITE_SIZE

SCREEN_MARGIN: Final[int] = 50
ASIDE_BAR_WIDTH: Final[int] = SPRITE_SIZE * 5 + 12

CONTENT_WIDTH: Final[int] = LEVEL_WIDTH + ASIDE_BAR_WIDTH
CONTENT_HEIGHT: Final[int] = LEVEL_HEIGHT
WIDTH: Final[int] = CONTENT_WIDTH + SCREEN_MARGIN * 2
HEIGHT: Final[int] = CONTENT_HEIGHT + SCREEN_MARGIN * 2
BORDER_WIDTH: Final[int] = 5

"""
Константы, описывающие размеры в игре
"""
