from typing import Dict, Generic, Optional, TypeVar, Union
from pygame import Surface
from packages.core.types import DrawableLifecycleMethods
from packages.core.screen import Screen
from packages.core.screen_part import ScreenPart


MT = TypeVar("MT")

_MachineState = Union[Screen, ScreenPart]


class StateMachine(DrawableLifecycleMethods, Generic[MT]):
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
        DrawableLifecycleMethods.__init__(self)
        Generic[MT].__init__(self, None)
        self.__screen__ = screen

    def init(self, *args, **kwargs):
        for key in self.__states__:
            self.__states__[key].init(*args, **kwargs)
        return super().init(*args, **kwargs)

    def change_state(self, state_id: MT, *args) -> None:
        """
        Метод смены состояния
        """
        if self.__active_state__:
            """
            Так как в текущий момент никакая сцена может быть не выбрана
            """
            self.__active_state__.deactivate()

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

    def deactivate(self, *args, **kwargs) -> None:
        """
        Метод дезактивации машины
        """
        if self.__active_state__:
            """
            Машину может не иметь никакого состояния на момент активации
            """
            self.__active_state__.deactivate(*args, **kwargs)
            self.__active_state__ = None

        return super().deactivate(*args, **kwargs)
