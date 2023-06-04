from pygame import Surface, sprite
from pygame.rect import Rect


class Sprite(sprite.Sprite):
    """
    Класс-надстройка над pygame-спрайтом
    """
    rect: Rect
    image: Surface

    def __init__(self, *groups: 'sprite._Group', image: Surface | None = None, **kwargs) -> None:
        super().__init__(*groups)
        self.image = image
        self.rect = image.get_rect()
