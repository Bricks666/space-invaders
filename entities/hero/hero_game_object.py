from pygame import image
from packages.core.game_object import GameObject
from packages.core.script import attach_scripts
from packages.core.math import VectorLike
from packages.core.view import attach_views, AttachSpriteOptions, SpritePositionOptions, Sprite
from .hero_script import HeroScript


@attach_scripts(HeroScript)
@attach_views(AttachSpriteOptions(
    sprite_class=Sprite,
    position_options=SpritePositionOptions(
        scale=VectorLike(1, 1)
    ),
    kwargs={
        'image': image.load('./assets/sprites/hero.png')
    }
))
class Hero(GameObject):
    """
    Класс игрока
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
