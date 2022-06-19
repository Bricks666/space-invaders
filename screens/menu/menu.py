from pygame import Surface
from components import Header
from consts.main import GAME_NAME
from packages.core import Screen
from .navigation import Navigation


class Menu(Screen):
    """
    Экран стартового меню
    """

    def __init__(self, screen: Surface) -> None:
        super().__init__(screen)
        self.__musics__.get("game_start").set_volume(0.2)

    def activate(self, *args, **kwargs) -> None:
        self.__musics__.get("game_start").play(-1)
        self.__parts__.append(Header(self.__screen__, GAME_NAME))
        self.__parts__.append(Navigation(self.__screen__))
        return super().activate(*args, **kwargs)

    def inactivate(self, *args, **kwargs) -> None:
        self.__musics__.get("game_start").stop()
        return super().inactivate(*args, **kwargs)
