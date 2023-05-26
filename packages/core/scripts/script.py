from abc import ABC
from typing import Generic, TypeVar
from .scriptable import Scriptable
from ..types import LifecycleMethods

GO = TypeVar('GO', bound="Scriptable")


class Script(Generic[GO], LifecycleMethods):
    _game_object: "GO"

    def __init__(self, game_object: "GO") -> None:
        Generic[GO].__init__(self, None)
        LifecycleMethods.__init__(self)
        self._game_object = game_object

    def kill(self):
        self._game_object = None
        pass
