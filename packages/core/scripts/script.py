from abc import ABC
from typing import Generic, TypeVar
from .scriptable import Scriptable
from ..types import BaseLifecycleMethods

GO = TypeVar('GO', bound="Scriptable")


class Script(Generic[GO], BaseLifecycleMethods):
    _game_object: "GO"
    __killed: bool

    def __init__(self, game_object: "GO") -> None:
        Generic[GO].__init__(self, None)
        BaseLifecycleMethods.__init__(self)
        self._game_object = game_object
        self.__killed = False

    def kill(self):
        if self.__killed:
            return

        self.__killed = True
        self._game_object.kill()
        self._game_object = None
