from typing import List, Dict
from pygame import Surface,  transform, sprite, mixer
from consts.main import STEP
from entities.bullet import Bullet
from packages.core.math import VectorLike
from packages.core.script import attach_scripts
from packages.core.view import attach_views, AttachSpriteOptions, SpritePositionOptions
from packages.core.game_object import GameObject
from consts import SPRITE_SIZE, BulletType
from .enemy_script import EnemyScript
from .enemy_view import EnemyView


@attach_scripts(EnemyScript)
@attach_views(AttachSpriteOptions(
    sprite_class=EnemyView,
    position_options=SpritePositionOptions(
        scale=VectorLike(0.8, 0.8)
    )
))
class Enemy(GameObject):
    """
    Враг
    """

    __musics__: Dict[str, mixer.Sound]

    _total_number: int
    _number: int

    def __init__(self, x: float, y: float, number: int, total_count: int, groups: List[sprite.Group], score: int = 50) -> None:
        super().__init__()
        # self._sprites.add(groups)
        # self.image = transform.scale(
        #     Enemy.__images__.get("enemy"), (SPRITE_SIZE * 0.7, SPRITE_SIZE * 0.7))
        # """
        # Масштабирование нужно, чтобы хитбокс не занимал все пространство спрайта
        # и было место между врагами
        # """
        # self.rect = self.image.get_rect()
        # self.rect.x = x
        # self.rect.y = y

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
