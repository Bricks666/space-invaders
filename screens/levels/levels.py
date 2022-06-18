from pygame import Surface
from packages.core import Screen
from screens.levels.header import Header
from screens.levels.list import List


class Levels(Screen):

    def __init__(self, screen: Surface) -> None:
        super().__init__(screen)

    def activate(self, *args, **kwargs) -> None:
        self.__parts__.append(Header(self.__screen__))
        self.__parts__.append(List(self.__screen__))
        return super().activate(*args, **kwargs)
