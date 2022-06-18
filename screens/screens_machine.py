from pygame import Surface
from typing import Dict, Literal
from packages.core import StateMachine, Screen
from screens.end import End
from screens.level import Level
from screens.levels import Levels
from screens.menu import Menu

_ScenesType = Literal["menu", "level", "end", "levels"]


class ScreensMachine(StateMachine[_ScenesType]):
    def __init__(self, screen: Surface) -> None:
        super().__init__(screen)

        self.__states__: Dict[_ScenesType, Screen] = {
            "level": Level(screen),
            "end": End(screen),
            "menu": Menu(screen),
            "levels": Levels(screen)
        }
