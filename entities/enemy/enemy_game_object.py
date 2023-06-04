from typing import List, Dict, ParamSpec
from pygame import Surface,   sprite, mixer, image
from consts.main import STEP
from entities.bullet import Bullet
from packages.core.math import VectorLike
from packages.core.script import attach_scripts
from packages.core.view import attach_views, AttachSpriteOptions, SpritePositionOptions, Sprite
from packages.core.game_object import GameObject
from consts import BulletType
from .enemy_script import EnemyScript

_P = ParamSpec('_P')


@attach_scripts(EnemyScript)
@attach_views(AttachSpriteOptions(
    sprite_class=Sprite,
    position_options=SpritePositionOptions(
        scale=VectorLike(0.8, 0.8)
    ),
    kwargs={
        'image': image.load('./assets/sprites/enemy.png')
    }
))
class Enemy(GameObject):
    """
    Враг
    """

    __musics__: Dict[str, mixer.Sound]

    _total_number: int
    _number: int

    def __init__(self, number: int, total_count: int, *args: _P.args, **kwargs: _P.kwargs) -> None:
        super().__init__(*args, **kwargs)
        # self.__musics__.get('step').set_volume(0.5)
        # self.__musics__.get("destroy").set_volume(0.5)

        self._total_number = total_count
        self._number = number


class EnemyBullet(Bullet):
    def __init__(self, image: Surface, x: float, y: float, groups: List[sprite.Group]) -> None:
        velocity = STEP * 3 * BulletType.ENEMY.value
        super().__init__(image, x, y, velocity, groups)

    def __collide__(self) -> bool:
        for s in self.__collidable__.sprites():
            if s == self or isinstance(s, (Enemy, EnemyBullet)):
                """
                Не дает застрелить себя, другую пулю врага или врага
                """
                continue
            if sprite.collide_rect(self, s):
                s.kill()
                return True
        return False
