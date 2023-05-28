from pygame import sprite
from typing import Any, Callable, TypeVar, Type, TypedDict, List, Dict
from .viewable import Viewable


GO = TypeVar('GO', bound=Viewable)

SC = TypeVar('SC', bound=sprite.Sprite)


class SpriteOptions(TypedDict):
    sprite_class: Type[SC] | None
    args: List[Any] | None
    kwargs: Dict[str, Any] | None


def attach_views(*sprites_options: SpriteOptions) -> Callable[[GO], GO]:
    def inner(game_object: GO) -> GO:
        orig_init = game_object.__init__

        def __init__(self: GO, *args, **kwargs) -> None:
            orig_init(self, *args, **kwargs)
            for sprite_options in sprites_options:
                sprite_class = sprite_options.get(
                    'sprite_class') or sprite.Sprite
                sargs = sprite_options.get('args') or []
                skwargs = sprite_options.get('kwargs') or {}
                s = sprite_class(*sargs, **skwargs)
                self._sprites.add(s)

        game_object.__init__ = __init__

        return game_object

    return inner
