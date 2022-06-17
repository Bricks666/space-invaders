from pygame import Surface
from packages.core import Screen
from scenes.level.aside import Aside
from scenes.level.levels_machine import LevelsMachine


class Level(Screen):

    def __init__(self, screen: Surface) -> None:
        super().__init__(screen)
        self.__parts__.append(LevelsMachine(screen))
        self.__parts__.append(Aside(screen))
