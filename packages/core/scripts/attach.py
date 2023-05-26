from typing import Callable, TypeVar, Type
from .script import Script
from .scriptable import Scriptable


GO = TypeVar('GO', bound=Scriptable)

def attach_scripts(*scripts: Type[Script]) -> Callable[[GO], GO]:
  def inner(game_object: GO) -> GO:
    orig_init = game_object.__init__

    def __init__(self: GO, *args, **kwargs) -> None:
      orig_init(self, *args, **kwargs)

      for script in scripts:
        self._scripts.add(script(self))

    game_object.__init__ = __init__

    return game_object

  return inner
