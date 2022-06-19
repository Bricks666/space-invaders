from pygame import Surface
from packages.core import Screen
from .level_header import LevelHeader
from .list import List


class Levels(Screen):
    """
    Экран выбора уровня
    """

    def __init__(self, screen: Surface) -> None:
        super().__init__(screen)
        self.__musics__.get("game_start").set_volume(0.05)

    def activate(self, *args, **kwargs) -> None:
        self.__musics__.get("game_start").play()
        self.__parts__.append(LevelHeader(self.__screen__))
        self.__parts__.append(List(self.__screen__))
        return super().activate(*args, **kwargs)

    def inactivate(self, *args, **kwargs) -> None:
        self.__musics__.get("game_start").stop()
        return super().inactivate(*args, **kwargs)
