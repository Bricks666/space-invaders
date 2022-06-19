from typing import Dict, Generic, Optional, TypeVar, Union
from pygame import Surface
from .activate import Activate
from .screen import Screen
from .screen_part import ScreenPart


MT = TypeVar("MT")

_MachineState = Union[Screen, ScreenPart]


class StateMachine(Activate, Generic[MT]):
    """
    Интерфейс для стейт-машины с некоторыми дополнениями
    """
    __screen__: Surface
    __active_state__: Optional[_MachineState] = None
    """
    Текущее состояние
    """
    __states__: Dict[MT, _MachineState] = {}
    """
    Список всех состояний
    """

    def __init__(self, screen: Surface):
        self.__screen__ = screen

    def change_state(self, state_id: MT, *args) -> None:
        """
        Метод смены состояния
        """
        if self.__active_state__:
            """
            Так как в текущий момент никакая сцена может быть не выбрана
            """
            self.__active_state__.inactivate()

        self.__active_state__ = self.__states__.get(state_id)
        self.__active_state__.activate(*args)

    def draw(self, *args) -> None:
        """
        Метод для отрисовки текущего состояния
        """
        if self.__active_state__:
            self.__active_state__.draw(*args)

    def update(self) -> None:
        """
        Метод для обновления текущего состояния
        """
        if self.__active_state__:
            self.__active_state__.update()

    def activate(self,  start_scene: Optional[MT] = None, *args, **kwargs) -> None:
        """
        Метод активации машины
        """
        if start_scene:
            """
            Машину можно активировать с начальной сценой
            """
            self.change_state(start_scene)

        return super().activate(*args, **kwargs)

    def inactivate(self, *args, **kwargs) -> None:
        """
        Метод дезактивации машины
        """
        if self.__active_state__:
            """
            Машину может не иметь никакого состояния на момент активации
            """
            self.__active_state__.inactivate(*args, **kwargs)
            self.__active_state__ = None

        return super().inactivate(*args, **kwargs)
