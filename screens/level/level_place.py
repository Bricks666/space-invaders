from pygame import Surface, Rect
from components import Primitive
from consts import BORDER_WIDTH, LEVEL_HEIGHT, LEVEL_WIDTH, SCREEN_MARGIN, BORDER_COLOR
from packages.core import ScreenPart
from packages.core.script import attach_scripts
from .level_place_script import LevelPlaceScript


@attach_scripts(LevelPlaceScript)
class LevelPlace(ScreenPart):

    def __init__(self, screen: Surface) -> None:
        rect = Rect(SCREEN_MARGIN, SCREEN_MARGIN, LEVEL_WIDTH, LEVEL_HEIGHT)
        super().__init__(screen, rect)

    def activate(self, level_id: int) -> None:
        self.level_id = level_id

        self.__create_border__()

        return super().activate()

    def __create_border__(self) -> None:
        """
        Метод создающий рамку вокруг уровня
        """
        top_left = (SCREEN_MARGIN - BORDER_WIDTH, SCREEN_MARGIN - BORDER_WIDTH)
        top_right = (SCREEN_MARGIN + LEVEL_WIDTH, SCREEN_MARGIN - BORDER_WIDTH)
        bottom_left = (SCREEN_MARGIN,
                       SCREEN_MARGIN + LEVEL_HEIGHT)
        top = Rect(*top_left, LEVEL_WIDTH + BORDER_WIDTH, BORDER_WIDTH)
        right = Rect(top_right, (BORDER_WIDTH,
                     LEVEL_HEIGHT + BORDER_WIDTH * 2))
        bottom = Rect(bottom_left, (LEVEL_WIDTH, BORDER_WIDTH))
        left = Rect(top_left, (BORDER_WIDTH, LEVEL_HEIGHT + BORDER_WIDTH * 2))
        top = Primitive(top, BORDER_COLOR)
        right = Primitive(right, BORDER_COLOR)
        bottom = Primitive(bottom, BORDER_COLOR)
        left = Primitive(left, BORDER_COLOR)
        self.__objects__.add(top, right, bottom, left)
