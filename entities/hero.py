from time import time
from typing import Dict, List
from pygame import transform, Surface, mixer, K_a, key, K_LEFT, K_d, K_RIGHT, K_SPACE, sprite
from consts import FIRE_COOLDOWN,  LEVEL_WIDTH, SCREEN_MARGIN, SPRITE_SIZE, STEP, BulletType,  Direction
from entities.bullet import Bullet
from packages.core import Collidable
from stores.lives import LivesStore
from packages.inject import Injector
from utils.loaders import sprite_loader


@Injector.inject(LivesStore, "__lives__")
class Hero(Collidable):
    __injected__: Dict[str, object]
    __lives__: LivesStore
    IMAGE: Surface = sprite_loader.load("hero.png")
    BULLET: Surface = sprite_loader.load("hero_bullet.png")
    KILL_SOUND: mixer.Sound
    DESTROY_SOUND: mixer.Sound

    def __init__(self, x: float, y: float, groups: List[sprite.Group]) -> None:
        super().__init__(*groups)
        self.image = transform.scale(
            Hero.IMAGE, (SPRITE_SIZE, SPRITE_SIZE))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.__start_x__ = x
        self.__start_y__ = y

        self.__last_fire__ = 0

        self.__lives__ = self.__injected__.get("__lives__")

    def update(self) -> None:
        if self.__collide__():
            return

        pressed_keys = key.get_pressed()
        if pressed_keys[K_a] or pressed_keys[K_LEFT]:
            self.__move__(Direction.LEFT)
        if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
            self.__move__(Direction.RIGHT)
        if pressed_keys[K_SPACE]:
            self.__fire__()

    def kill(self) -> None:
        self.__lives__.decrement_lives()
        if not self.__lives__.get_lives():
            Hero.KILL_SOUND.play()
            return super().kill()
        Hero.DESTROY_SOUND.play()
        self.rect.x = self.__start_x__
        self.rect.y = self.__start_y__

    def __move__(self, direction: Direction) -> None:
        if self.__can_move__(direction):
            self.rect.x += STEP * direction.value

    def __can_move__(self, direction: Direction) -> bool:
        match direction:
            case Direction.LEFT:
                return self.rect.x > SCREEN_MARGIN
            case Direction.RIGHT:
                return self.rect.x < LEVEL_WIDTH + SCREEN_MARGIN - SPRITE_SIZE

    def __collide__(self) -> bool:
        return super().__collide__()

    def __fire__(self) -> None:
        current_time = time()
        if self.__last_fire__ + FIRE_COOLDOWN <= current_time:
            HeroBullet(Hero.BULLET, self.rect.centerx, self.rect.y,
                       self.groups())
            self.__last_fire__ = current_time


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
