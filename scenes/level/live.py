from pygame import Surface, sprite, transform
from consts import SPRITE_SIZE
from utils.loaders import sprite_loader


class Live(sprite.Sprite):
    image: Surface = transform.scale(sprite_loader.load(
        "hero.png"), (SPRITE_SIZE * 0.8, SPRITE_SIZE * 0.8))

    def __init__(self, x: float, y: float) -> None:
        super().__init__()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
