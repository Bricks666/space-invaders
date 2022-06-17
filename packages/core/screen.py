from abc import ABC,  abstractmethod
from typing import Dict, List
from pygame import Surface, mixer
from packages.core.screen_part import ScreenPart


class Screen(ABC):
    __screen__: Surface
    __musics__: Dict[str, mixer.Sound]
    __parts__: List[ScreenPart]

    def __init__(self, screen: Surface) -> None:
        self.__screen__ = screen
        self.__parts__ = []
        self.__musics__ = {}

    def draw(self) -> None:
        for part in self.__parts__:
            part.draw()

    def update(self) -> None:
        for part in self.__parts__:
            part.update()

    def select(self) -> None:
        for part in self.__parts__:
            part.select()

    def unselect(self) -> None:
        for part in self.__parts__:
            part.unselect()
