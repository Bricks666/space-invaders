from time import time
from typing import Dict
import pygame
from consts.main import FIRE_COOLDOWN,  LEVEL_WIDTH, SCREEN_MARGIN, SPRITE_SIZE, STEP, BulletType,  Direction
from entities.bullet import Bullet
from entities.collidable import Collidable
from stores.lives import Lives, lives
from stores.main import inject

from utils.loaders import sprite_loader


@inject(lives, "__lives__")
class Hero(Collidable):
    __injected__: Dict
    __lives__: Lives
    IMAGE: pygame.Surface = sprite_loader.load("hero.png")
    BULLET: pygame.Surface = sprite_loader.load("hero_bullet.png")
    KILL_SOUND: pygame.mixer.Sound
    DESTROY_SOUND: pygame.mixer.Sound

    def __init__(self, x: float, y: float):
        super().__init__()
        self.image = pygame.transform.scale(
            Hero.IMAGE, (SPRITE_SIZE, SPRITE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.__start_x__ = x
        self.__start_y__ = y
        self.__lives__ = self.__injected__.get("__lives__")
        self.__last_fire__ = 0

    def update(self) -> None:
        is_collided = self.__collide__()
        if is_collided:
            return
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            self.__move__(Direction.LEFT)
        if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            self.__move__(Direction.RIGHT)
        if pressed_keys[pygame.K_SPACE]:
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

    def __fire__(self):
        current_time = time()
        if self.__last_fire__ + FIRE_COOLDOWN <= current_time:
            HeroBullet(Hero.BULLET, self.rect.centerx, self.rect.y,
                       self.groups()[0])
            self.__last_fire__ = current_time


class HeroBullet(Bullet):
    def __init__(self, image: pygame.Surface, x: float, y: float, *group):
        super().__init__(image, x, y, BulletType.HERO, *group)

    def __collide__(self) -> bool:
        for sprite in self.__collidable__.sprites():
            if sprite == self or isinstance(sprite, (Hero, HeroBullet)):
                continue
            if pygame.sprite.collide_rect(self, sprite):
                self.kill()
                sprite.kill()
                return True
        return False
