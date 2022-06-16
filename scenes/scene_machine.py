from pygame import KEYDOWN, Surface, key, event
from typing import Dict, Literal
from packages.core import Machine, Scene
from scenes.level import Level
from scenes.levels_machine import LevelsMachine

_ScenesType = Literal["menu", "level"]


class ScenesMachine(Machine[_ScenesType]):
    def __init__(self, screen: Surface) -> None:
        super().__init__(screen)

        self.__scenes__: Dict[_ScenesType, Scene] = {
            "menu": Level(screen, "a"),
            "level": LevelsMachine(screen)
        }

    def change_scene(self, scene_id: _ScenesType) -> None:
        if self.__active_scene_id__ == scene_id:
            return
        if self.__active_scene__:
            self.__active_scene__.unselect()
        self.__active_scene__ = self.__scenes__.get(scene_id)
        self.__active_scene__.select()
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
