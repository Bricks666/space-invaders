from typing import Dict
from pygame import Surface, sprite, mixer, rect
from pygame.rect import Rect


class Sprite(sprite.Sprite):
    """
    Класс-надстройка над pygame-спрайтом
    """
    rect: Rect

    __musics__: Dict[str, mixer.Sound] = {}
    __images__: Dict[str, Surface] = {}

    def __init__(self, *groups: 'sprite._Group') -> None:
        super().__init__(*groups)
        self.rect = sprite.Rect(0, 0, 0, 0)

    @classmethod
    def set_image(cls, name: str, image: Surface) -> None:
        cls.__images__.update([[name, image]])

    @classmethod
    def set_music(cls, name: str, music: mixer.Sound) -> None:
        cls.__musics__.update([[name, music]])
