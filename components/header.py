from typing import Optional
from pygame import Rect, Surface
from consts.sizes import CONTENT_WIDTH, SCREEN_MARGIN
from packages.core import ScreenPart
from components.text import Text


class Header(ScreenPart):
    __text__: str

    def __init__(self, screen: Surface, text: str, rect: Optional[Rect] = None) -> None:
        _rect = rect or Rect(SCREEN_MARGIN, SCREEN_MARGIN,
                             CONTENT_WIDTH, SCREEN_MARGIN)
        super().__init__(screen, _rect)

        self.__text__ = text

    def activate(self, *args, **kwargs) -> None:
        self.__create_header__()
        return super().activate(*args, **kwargs)

    def __create_header__(self) -> None:
        header = Text(self.__text__, 0, 0, "large")
        header.rect.center = self.rect.center
        self.__all_sprites__.add(header)
