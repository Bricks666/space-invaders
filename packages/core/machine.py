from typing import Dict, Generic, Optional, TypeVar, Union
from pygame import Surface
from packages.core.screen import Screen
from packages.core.screen_part import ScreenPart


MT = TypeVar("MT")

_MachineState = Union[Screen, ScreenPart]


class StateMachine(Generic[MT]):
    __screen__: Surface
    __active_scene__: Optional[_MachineState]
    __scenes__: Dict[MT, _MachineState]
    __active_scene_id__: Optional[MT]

    def __init__(self, screen: Surface):
        self.__screen__ = screen
        self.__active_scene__ = None
        self.__active_scene_id__ = None
        self.__scenes__ = dict()

    def change_scene(self, scene_id: MT) -> None:
        if self.__active_scene__:
            self.__active_scene__.unselect()

        self.__active_scene__ = self.__scenes__.get(scene_id)
        self.__active_scene_id__ = scene_id
        self.__active_scene__.select()

    def draw(self) -> None:
        if self.__active_scene__:
            self.__active_scene__.draw()

    def update(self) -> None:
        if self.__active_scene__:
            self.__active_scene__.update()

    def restart(self) -> None:
        pass

    def on(self,  start_scene: Optional[MT] = None) -> None:
        if start_scene:
            self.change_scene(start_scene)

    def off(self) -> None:
        if self.__active_scene__:
            self.__active_scene__.unselect()
            self.__active_scene__ = self.__active_scene_id__ = None
