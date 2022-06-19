from typing import Dict, List
from pygame import Surface, mixer
from packages.core.activate import Activate
from packages.core.screen_part import ScreenPart


class Screen(Activate):
    __screen__: Surface
    __musics__: Dict[str, mixer.Sound] = {}
    __parts__: List[ScreenPart]

    def __init__(self, screen: Surface) -> None:
        super().__init__()
        self.__screen__ = screen
        self.__parts__ = []

    def draw(self, *args) -> None:
        for part in self.__parts__:
            part.draw(*args)

    def update(self) -> None:
        self.__control_events__()
        for part in self.__parts__:
            part.update()

    def activate(self, *args, **kwargs) -> None:
        for part in self.__parts__:
            part.activate(*args, **kwargs)

    def inactivate(self, *args, **kwargs) -> None:
        for part in self.__parts__:
            part.inactivate(*args, **kwargs)
        self.__parts__.clear()

    def __control_events__(self) -> None:
        pass

    @classmethod
    def set_music(cls, name: str, music: mixer.Sound) -> None:
        cls.__musics__.update([[name, music]])
