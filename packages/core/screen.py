from typing import Dict, List
from pygame import Surface, mixer
from packages.core.activate import Activate
from packages.core.screen_part import ScreenPart


class Screen(Activate):
    """
    Абстрактный класс описывающий экран
    """
    __screen__: Surface
    __musics__: Dict[str, mixer.Sound] = {}
    """
    Музыка экрана
    """
    __parts__: List[ScreenPart]
    """
    Части экрана
    """

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
        """
        Очищение списка частей
        Так как он формируется на каждую активацию
        """

    def __control_events__(self) -> None:
        """
        Метод контроля событий на уровне сцены
        """
        pass

    @classmethod
    def set_music(cls, name: str, music: mixer.Sound) -> None:
        """
        Метод для сохранения музыки
        """
        cls.__musics__.update([[name, music]])
