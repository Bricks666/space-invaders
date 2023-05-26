from typing import Set
from .script import *
from ..types import LifecycleMethods


class Scriptable(LifecycleMethods):
    _scripts: Set["Script"]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__()
        self._scripts = set()

    def activate(self, *args, **kwargs):
        for script in self._scripts:
            script.activate()

    def init(self, *args, **kwargs):
        for script in self._scripts:
            script.init()

    def update(self, *args, **kwargs):
        for script in self._scripts:
            script.update()

    def deactivate(self, *args, **kwargs):
        for script in self._scripts:
            script.deactivate()

    def kill(self, *args, **kwargs):
        for script in self._scripts:
            script.kill()

        self._scripts = set()
