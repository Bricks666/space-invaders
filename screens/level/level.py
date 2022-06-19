from pygame import Surface
from packages.core import Screen
from .aside import Aside
from .level_place import LevelPlace


class Level(Screen):
    """
    Экран уровня
    """

    def __init__(self, screen: Surface) -> None:
        super().__init__(screen)

        self.__musics__.get("level_start").set_volume(0.2)

    def activate(self, *args) -> None:
        self.__musics__.get("level_start").play()
        self.__parts__.append(LevelPlace(self.__screen__))
        self.__parts__.append(Aside(self.__screen__))
        return super().activate(*args)

    def inactivate(self, *args, **kwargs) -> None:
        self.__musics__.get("level_start").stop()
        return super().inactivate(*args, **kwargs)
