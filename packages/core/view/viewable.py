from pygame import sprite, Surface
from ..base.lifecycle import DrawableLifecycleMethods
from ..math import AABB
from .sprite import *
from .types import SpritePositionOptions


class Viewable(AABB, DrawableLifecycleMethods):
    _sprites: sprite.Group
    _position_options_dict: Dict['Sprite', SpritePositionOptions]

    def __init__(self, *args, **kwargs) -> None:
        AABB.__init__(self, *args, **kwargs)
        DrawableLifecycleMethods.__init__(self, *args, **kwargs)

        self._sprites = sprite.Group()
        self._position_options_dict = {}

    def update(self, *args, **kwargs) -> None:
        if self._mutated:
            self._reflow()
        return super().update(*args, **kwargs)

    def draw(self, screen: Surface, *args, **kwargs):
        self._sprites.draw(screen, *args, **kwargs)

    def kill(self, *args, **kwargs) -> None:
        for sprite in self._sprites:
            sprite.kill()
        return super().kill(*args, **kwargs)

    def _reflow(self):
        for sprite in self._sprites:
            options = self._position_options_dict.get(sprite)
            if not options:
                continue

            scale, *_ = options

            center = self.center_x, self.center_y
            sizes = scale.x * self.width, scale.y * self.height

            sprite.rect.center = center
            sprite.rect.size = sizes
        self._mutated = False
