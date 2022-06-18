from typing import Dict, Generic, Optional, TypeVar, Union
from pygame import Surface
from packages.core.activate import Activate
from packages.core.screen import Screen
from packages.core.screen_part import ScreenPart


MT = TypeVar("MT")

_MachineState = Union[Screen, ScreenPart]


class StateMachine(Activate, Generic[MT]):
    __screen__: Surface
    __active_state__: Optional[_MachineState] = None
    __states__: Dict[MT, _MachineState] = {}
    __active_scene_id__: Optional[MT] = None

    def __init__(self, screen: Surface):
        self.__screen__ = screen

    def change_state(self, state_id: MT, *args) -> None:
        if self.__active_state__:
            self.__active_state__.inactivate()

        self.__active_state__ = self.__states__.get(state_id)
        self.__active_scene_id__ = state_id
        self.__active_state__.activate(*args)

    def draw(self, *args) -> None:
        if self.__active_state__:
            self.__active_state__.draw(*args)

    def update(self) -> None:
        if self.__active_state__:
            self.__active_state__.update()

    def activate(self,  start_scene: Optional[MT] = None, *args, **kwargs) -> None:
        if start_scene:
            self.change_state(start_scene)

        return super().activate(*args, **kwargs)

    def inactivate(self, *args, **kwargs) -> None:
        if self.__active_state__:
            self.__active_state__.inactivate(*args, **kwargs)
            self.__active_state__ = self.__active_scene_id__ = None

        return super().inactivate(*args, **kwargs)
