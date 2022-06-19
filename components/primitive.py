from pygame import Color, Rect, Surface
from packages.core import Sprite


class Primitive(Sprite):
    """
    Класс описывающий прямоугольный примитив
    """

    def __init__(self, rect: Rect, color: Color) -> None:
        super().__init__()
        self.image = Surface(rect.size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = rect.topleft
