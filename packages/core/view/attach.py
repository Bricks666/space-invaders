from typing import Any, Callable, TypeVar, Type, NamedTuple, List, Dict
from .viewable import *
from .sprite import *
from .types import SpritePositionOptions


GO = TypeVar('GO', bound='Viewable')

SC = TypeVar('SC', bound='Sprite')


class AttachSpriteOptions(NamedTuple):
    sprite_class: Type[SC]
    position_options: SpritePositionOptions = SpritePositionOptions()
    args: List[Any] = []
    kwargs: Dict[str, Any] = {}


def attach_views(*sprites_options: AttachSpriteOptions) -> Callable[[GO], GO]:
    def inner(game_object: GO) -> GO:
        orig_init = game_object.__init__

        def __init__(self: GO, *args, **kwargs) -> None:
            orig_init(self, *args, **kwargs)

            for sprite_options in sprites_options:
                sprite_class = sprite_options.sprite_class

                sargs = sprite_options.args
                skwargs = sprite_options.kwargs
                position_options = sprite_options.position_options

                sprite = sprite_class(*sargs, **skwargs)
                self._position_options_dict[sprite] = position_options
                self._sprites.add(sprite)
            self._reflow()
        game_object.__init__ = __init__

        return game_object

    return inner
