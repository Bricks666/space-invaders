from typing import Dict
from pygame import Surface
from packages.core import Screen
from packages.inject import Injector
from screens.level.aside import Aside
from screens.level.levels_machine import LevelsMachine
from stores.level import LevelStore


@Injector.inject(LevelStore, "__level__")
class Level(Screen):
    __injected__: Dict[str, object]
    __level__: LevelStore

    def __init__(self, screen: Surface) -> None:
        super().__init__(screen)

        self.__level__ = self.__injected__.get("__level__")

    def activate(self, *args) -> None:
        self.__musics__.get("start").play()
        self.__parts__.append(LevelsMachine(self.__screen__))
        self.__parts__.append(Aside(self.__screen__))

        current_level = self.__level__.get_current_level()
        current_level_id = current_level and current_level.level_id

        return super().activate(current_level_id, *args)
