from time import time
from typing import Dict, List
from pygame import transform, Surface, mixer, sprite
from consts import FIRE_COOLDOWN,  LEVEL_WIDTH, SCREEN_MARGIN, SPRITE_SIZE, STEP, BulletType
from entities.bullet import Bullet
from packages.core import Entity, Direction
from stores.lives import LivesStore
from packages.inject import Injector


@Injector.inject(LivesStore, "__lives__")
class Hero(Entity):
    __injected__: Dict[str, object]
    __lives__: LivesStore

    def __init__(self, x: float, y: float, groups: List[sprite.Group]) -> None:
        super().__init__(*groups)
        self.image = transform.scale(
            self.__images__.get("hero"), (SPRITE_SIZE, SPRITE_SIZE))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.__start_x__ = x
        self.__start_y__ = y
        self.__speed__ = STEP

        self.__last_fire__ = 0

        self.__lives__ = self.__injected__.get("__lives__")

    def update(self) -> None:
        if self.__collide__():
            return
        return super().update()

    def kill(self) -> None:
        self.__lives__.decrement_lives()

        if not self.__lives__.get_lives():
            self.__musics__.get("kill").play()
            return super().kill()

        self.__musics__.get("destroy").play()
        self.rect.x = self.__start_x__
        self.rect.y = self.__start_y__

    def move(self, direction: Direction) -> None:
        if self.__can_move__(direction):
            self.rect.move_ip(self.__speed__ * direction.value, 0)

    def fire(self) -> None:
        current_time = time()
        if self.__last_fire__ + FIRE_COOLDOWN <= current_time:
            HeroBullet(self.__images__.get("hero_bullet"), self.rect.centerx, self.rect.y,
                       self.groups())
            self.__last_fire__ = current_time

    def __can_move__(self, direction: Direction) -> bool:
        match direction:
            case Direction.LEFT:
                return self.rect.x > SCREEN_MARGIN
            case Direction.RIGHT:
                return self.rect.x < LEVEL_WIDTH + SCREEN_MARGIN - SPRITE_SIZE

    def __collide__(self) -> bool:
        return super().__collide__()


class HeroBullet(Bullet):
    def __init__(self, image: Surface, x: float, y: float, groups: List[sprite.Group]) -> None:
        super().__init__(image, x, y, BulletType.HERO, groups)

    def __collide__(self) -> bool:
        for s in self.__collidable__.sprites():
            if s == self or isinstance(s, (Hero, HeroBullet)):
                continue
            if sprite.collide_rect(self, s):
                self.kill()
                s.kill()
                return True
        return False
