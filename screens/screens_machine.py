from pygame import Surface
from typing import Dict, Literal
from packages.core import StateMachine, Screen
from screens.end import End
from screens.level import Level
from screens.menu import Menu

_ScenesType = Literal["menu", "level", "end"]


class ScreensMachine(StateMachine[_ScenesType]):
    def __init__(self, screen: Surface) -> None:
        super().__init__(screen)

        """ Написать меню """
        self.__states__: Dict[_ScenesType, Screen] = {
            "level": Level(screen),
            "end": End(screen),
            "menu": Menu(screen)
        }

    def restart(self) -> None:
        if self.__active_state__:
            self.__active_state__.inactivate()
            self.__active_state__.activate()
