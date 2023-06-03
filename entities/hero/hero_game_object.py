from typing import List
from pygame import sprite
from packages.core.game_object import GameObject
from packages.core.script import attach_scripts
from packages.core.math import VectorLike
from packages.core.view import attach_views, AttachSpriteOptions, SpritePositionOptions
from .hero_script import HeroScript
from .hero_sprite import HeroSprite


@attach_scripts(HeroScript)
@attach_views(AttachSpriteOptions(
    sprite_class=HeroSprite,
    position_options=SpritePositionOptions(
        scale=VectorLike(0.6, 0.6)
    )
))
class Hero(GameObject):
    """
    Класс игрока
    """

    def __init__(self, x: float, y: float, groups: List[sprite.Group]) -> None:
        super().__init__()
        # self.image = self.__images__.get("hero")
        # self.__musics__.get("explosion").set_volume(0.2)

        # self.rect = self.image.get_rect()
        # self.rect.x = x
        # self.rect.y = y
