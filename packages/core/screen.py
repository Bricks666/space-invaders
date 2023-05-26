from typing import Dict, List
from pygame import Surface, mixer
from packages.core.types import LifecycleMethods
from packages.core.screen_part import ScreenPart


class Screen(LifecycleMethods):
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
        """
        Метод отрисовки экрана

        Отрисовывает все части экрана
        """
        for part in self.__parts__:
            part.draw(*args)

    def update(self) -> None:
        """
        Метод обновления экрана

        Обновляет все части экрана и контролирует события
        """
        self.__control_events__()
        for part in self.__parts__:
            part.update()

    def activate(self, *args, **kwargs) -> None:
        """
        Метод для активации экрана

        Активирует все свои части
        """
        for part in self.__parts__:
            part.activate(*args, **kwargs)

    def deactivate(self, *args, **kwargs) -> None:
        """
        Метод дезактивации экрана

        Дезактивирует все свои части и очищает их список
        """
        for part in self.__parts__:
            part.deactivate(*args, **kwargs)
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
