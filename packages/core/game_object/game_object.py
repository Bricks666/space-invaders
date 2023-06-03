from typing import Set
from ..math import AABB, Vector
from ..script import Scriptable
from ..view import Viewable
from .group import *


class GameObject(AABB, Scriptable, Viewable):
    name: str
    __killed: bool
    _groups: Set['Group']

    def __init__(self, start: Vector, end: Vector, *args, **kwargs) -> None:
        AABB.__init__(self, start, end)
        Scriptable.__init__(self, *args, **kwargs)
        Viewable.__init__(self, *args, **kwargs)
        self.__killed = False
        self._groups = set()

    def activate(self, *args, **kwargs):
        Scriptable.activate(self, *args, **kwargs)
        Viewable.activate(self, *args, **kwargs)

    def update(self, *args, **kwargs):
        Scriptable.update(self, *args, **kwargs)
        Viewable.update(self, *args, **kwargs)

    def deactivate(self, *args, **kwargs):
        Scriptable.activate(self, *args, **kwargs)
        Viewable.activate(self, *args, **kwargs)

    def kill(self, *args, **kwargs) -> None:
        if self.__killed:
            return
        self.__killed = True
        Scriptable.kill(self, *args, **kwargs)
        Viewable.kill(self, *args, **kwargs)

    def add_group(self, group: 'Group') -> None:
        self._groups.add(group)

    def has_group(self, group: 'Group') -> None:
        self._groups.add(group)
