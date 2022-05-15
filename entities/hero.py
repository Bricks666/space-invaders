from time import time
import pygame
from consts.main import FIRE_COOLDOWN, SPRITE_SIZE, STEP, BulletType,  Direction
from entities.bullet import Bullet
from entities.collidable import Collidable

from utils.sprite_loader import SpriteLoader


class Hero(Collidable):
    IMAGE: pygame.Surface = SpriteLoader.load("hero.png")
    BULLET: pygame.Surface = SpriteLoader.load("hero_bullet.png")

    def __init__(self, x: float, y: float):
        super().__init__()
        self.image = pygame.transform.scale(
            Hero.IMAGE, (SPRITE_SIZE, SPRITE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
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

    def __move__(self, direction: Direction):
        self.rect.x += STEP * direction.value

    def __collide__(self) -> bool:
        return super().__collide__()

    def __fire__(self):
        current_time = time()
        if self.__last_fire__ + FIRE_COOLDOWN <= current_time:
            HeroBullet(Hero.BULLET, self.rect.x, self.rect.y,
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
