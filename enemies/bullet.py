import pygame
from consts.main import SPRITE_SIZE

from utils.sprite_loader import SpriteLoader


class Bullet(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface, x: float, y: float):
        super().__init__()
        self.image = pygame.transform.scale(image, (SPRITE_SIZE, SPRITE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update():
      pass



class HeroBullet(Bullet):
    IMAGE = SpriteLoader.load("hero_bullet.png")
    def __init__(self, x: float, y: float):
        super().__init__(HeroBullet.IMAGE, x, y)
        pass
