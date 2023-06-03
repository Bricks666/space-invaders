from packages.core.view import Sprite
from pygame import image


class HeroSprite(Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image = image.load('./assets/sprites/hero.png')
        self.rect = self.image.get_rect()
