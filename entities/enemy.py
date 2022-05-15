from time import time
from typing import Dict
import pygame
from entities.bullet import Bullet
from entities.collidable import Collidable
from stores.main import inject
from stores.scores import Scores, scores
from utils.loaders import sprite_loader
from consts.main import LEVEL_WIDTH, SCREEN_MARGIN, SPRITE_SIZE, BulletType,  Direction


@inject(scores, "__scores__")
class Enemy(Collidable):
    __injected__: Dict
    __scores__: Scores
    IMAGE: pygame.Surface = sprite_loader.load("enemy.png")
    BULLET: pygame.Surface = sprite_loader.load("enemy_bullet.png")
    DURATION: float = 0.5
    DESTROY: pygame.mixer.Sound

    def __init__(self, x: float, y: float, number: int, total_count: int, scores: int = 50):
        super().__init__()
        self.image = pygame.transform.scale(
            Enemy.IMAGE, (SPRITE_SIZE * 0.7, SPRITE_SIZE * 0.7))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.__offset_right__ = SPRITE_SIZE * (total_count - number)
        self.__offset_left__ = SPRITE_SIZE * number
        self.__direction__ = Direction.LEFT
        self.__end__ = False
        self.__last_move__ = time()
        self.__score__ = scores
        self.__scores__ = self.__injected__.get("__scores__")

    def update(self) -> None:
        is_collided = self.__collide__()
        if is_collided:
            return
        current_time = time()
        can_move = self.__can_move__(current_time)
        if not can_move:
            return
        self.__last_move__ = current_time
        if self.__end__:
            self.__change_direction__()
            self.__down__()
        self.rect.x += SPRITE_SIZE / 4 * self.__direction__.value
        self.__end__ = self.__check_end__()

    def __check_end__(self) -> bool:
        return self.rect.x <= SCREEN_MARGIN + self.__offset_left__ or self.rect.x >= LEVEL_WIDTH + SCREEN_MARGIN - self.__offset_right__

    def __change_direction__(self) -> None:
        self.__direction__ = Direction.RIGHT if self.__direction__ == Direction.LEFT else Direction.LEFT
        self.__end__ = False

    def __can_move__(self, current_time):
        return self.__last_move__ + Enemy.DURATION <= current_time

    def __down__(self) -> None:
        self.rect.y += SPRITE_SIZE / 2

    def __collide__(self) -> bool:
        return super().__collide__()

    def fire(self) -> None:
        EnemyBullet(Enemy.BULLET, self.rect.centerx, self.rect.y,
                    self.groups()[0])

    def kill(self) -> None:
        Enemy.DESTROY.play()
        self.__scores__.add(self.__score__)
        return super().kill()


class EnemyBullet(Bullet):
    def __init__(self, image: pygame.Surface, x: float, y: float, *group):
        super().__init__(image, x, y, BulletType.ENEMY, *group)

    def __collide__(self) -> bool:
        for sprite in self.__collidable__.sprites():
            if sprite == self or isinstance(sprite, (Enemy, EnemyBullet)):
                continue
            if pygame.sprite.collide_rect(self, sprite):
                self.kill()
                sprite.kill()
                return True
        return False
