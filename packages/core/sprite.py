from typing import Dict
from pygame import Surface, sprite, mixer


class Sprite(sprite.Sprite):
    """
    Класс-надстройка над pygame-спрайтом

    Добавляет музыку и изображения к нему
    """
    __musics__: Dict[str, mixer.Sound] = {}
    __images__: Dict[str, Surface] = {}

    @classmethod
    def set_image(cls, name: str, image: Surface) -> None:
        cls.__images__.update([[name, image]])

    @classmethod
    def set_music(cls, name: str, music: mixer.Sound) -> None:
        cls.__musics__.update([[name, music]])
