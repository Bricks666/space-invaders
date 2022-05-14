from time import time
import pygame
from consts.main import FIRE_COOLDOWN, SPRITE_SIZE, STEP, Direction
from enemies.bullet import HeroBullet

from utils.sprite_loader import SpriteLoader


class Hero(pygame.sprite.Sprite):
    IMAGE: pygame.Surface = SpriteLoader.load("hero.png")

    def __init__(self, x: float, y: float):
        super().__init__()
        self.image = pygame.transform.scale(
            Hero.IMAGE, (SPRITE_SIZE, SPRITE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.__last_fire = 0

    def update(self) -> None:
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            self.__move(Direction.LEFT)
        if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            self.__move(Direction.RIGHT)
        if pressed_keys[pygame.K_SPACE] or pressed_keys[pygame.MOUSEBUTTONDOWN]:
            self.__fire()

    def __move(self, direction: Direction):
        self.rect.x += STEP * direction.value

    def __fire(self):
        current_time = time()
        if self.__last_fire + FIRE_COOLDOWN <= current_time:
            start_x = self.rect.centerx
            HeroBullet(start_x, self.rect.y, self.groups()[0])
            self.__last_fire = current_time
