from pygame import KEYDOWN, Surface, event
from typing import Dict, Literal
from packages.core import StateMachine, Screen
from scenes.end import End
from scenes.level import Level

_ScenesType = Literal["menu", "level", "end"]


class ScenesMachine(StateMachine[_ScenesType]):
    def __init__(self, screen: Surface) -> None:
        super().__init__(screen)

        """ Написать меню """
        self.__scenes__: Dict[_ScenesType, Screen] = {
            "level": Level(screen),
            "end": End(screen)
        }

    def change_scene(self, scene_id: _ScenesType, *args) -> None:
        if self.__active_scene_id__ == scene_id:
            return
        if self.__active_scene__:
            self.__active_scene__.unselect()
        self.__active_scene__ = self.__scenes__.get(scene_id)
        self.__active_scene__.select(*args)
        self.__active_scene_id__ = scene_id

    def update(self) -> None:
        self.__control_events__()
        return super().update()

    def restart(self) -> None:
        if self.__active_scene__:
            self.__active_scene__.unselect()
            self.__active_scene__.select()

    def __control_events__(self) -> None:
        if self.__active_scene_id__ == "menu":
            for e in event.get(KEYDOWN):
                pass
