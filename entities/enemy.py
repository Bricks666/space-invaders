import pygame
from entities.bullet import Bullet
from entities.collidable import Collidable
from utils.sprite_loader import SpriteLoader
from consts.main import SPRITE_SIZE, WIDTH, BulletType,  Direction


class Enemy(Collidable):
    IMAGE: pygame.Surface = SpriteLoader.load("enemy.png")
    BULLET: pygame.Surface = SpriteLoader.load("enemy_bullet.png")

    def __init__(self, x: float, y: float, number: int, total_count: int):
        super().__init__()
        self.image = pygame.transform.scale(
            Enemy.IMAGE, (SPRITE_SIZE, SPRITE_SIZE))
        self.__offset_left__ = SPRITE_SIZE * number
        self.__offset_right__ = SPRITE_SIZE * (total_count - number)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.__direction__ = Direction.LEFT
        self.__end__ = False

    def update(self) -> None:
        is_collided = self.__collide__()
        if is_collided:
            return
        if self.__end__:
            self.__change_direction__()
            self.__down__()
        self.rect.x += SPRITE_SIZE / 4 * self.__direction__.value
        self.__end__ = self.__check_end__()

    def __check_end__(self) -> bool:
        return self.rect.x <= 0 + self.__offset_left__ or self.rect.x >= WIDTH - self.__offset_right__

    def __change_direction__(self) -> None:
        self.__direction__ = Direction.RIGHT if self.__direction__ == Direction.LEFT else Direction.LEFT
        self.__end__ = False

    def __down__(self) -> None:
        self.rect.y += SPRITE_SIZE / 2

    def __collide__(self) -> bool:
        return super().__collide__()

    def fire(self) -> None:
        EnemyBullet(Enemy.BULLET, self.rect.x, self.rect.y,
                    self.groups()[0])


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
