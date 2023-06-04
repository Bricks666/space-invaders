from typing import Set
from ..base.lifecycle import BaseLifecycleMethods
from .script import *


class Scriptable(BaseLifecycleMethods):
    _scripts: Set["Script"]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._scripts = set()

    def activate(self, *args, **kwargs) -> None:
        for script in self._scripts:
            script.activate()

    def init(self, *args, **kwargs) -> None:
        for script in self._scripts:
            script.init()

    def update(self, *args, **kwargs) -> None:
        for script in self._scripts:
            script.update()

    def deactivate(self, *args, **kwargs) -> None:
        for script in self._scripts:
            script.deactivate()

    def kill(self, *args, **kwargs) -> None:
        for script in self._scripts:
            script.kill()

        self._scripts = set()
