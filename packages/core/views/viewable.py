from pygame import sprite, Surface
from typing import List
from ..types import DrawableLifecycleMethods


class Viewable(DrawableLifecycleMethods):
    _sprites: sprite.Group

    def __init__(self, sprites: None | List[sprite.Sprite] = [], *args, **kwargs) -> None:
        self._sprites = sprite.Group(*sprites)
        DrawableLifecycleMethods.__init__(self, *args, **kwargs)

    def draw(self, screen: Surface, *args, **kwargs):
        self._sprites.draw(screen, *args, **kwargs)
