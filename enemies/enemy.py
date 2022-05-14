import pygame
from enemies.bullet import HeroBullet
from utils.sprite_loader import SpriteLoader
from consts.main import SPRITE_SIZE, STEP, WIDTH, Direction


class Enemy(pygame.sprite.Sprite):
    IMAGE = SpriteLoader.load("enemy.png")

    def __init__(self, x: float, y: float, number: int, total_count: int):
        super().__init__()
        self.image = pygame.transform.scale(
            Enemy.IMAGE, (SPRITE_SIZE, SPRITE_SIZE))
        self.__offset_left = SPRITE_SIZE * number
        self.__offset_right = SPRITE_SIZE * (total_count - number)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.__direction = Direction.LEFT
        self.__end = False

    def update(self):
        if self.__end:
            self.__change_direction()
            self.__down()
        self.rect.x += STEP * self.__direction.value
        print("UPDATE")
        self.__end = self.__check_end()

    def __check_end(self):
        return self.rect.x <= 0 + self.__offset_left or self.rect.x >= WIDTH - self.__offset_right

    def __change_direction(self):
        self.__direction = Direction.RIGHT if self.__direction == Direction.LEFT else Direction.LEFT
        self.__end = False

    def __down(self):
        self.rect.y += STEP

    def shot(self):
        start_x = self.rect.centerx
        HeroBullet(start_x, self.rect.y, self.groups()[0])
