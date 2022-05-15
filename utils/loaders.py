from abc import ABCMeta, abstractmethod
from typing import List
import pygame


class Loader(metaclass=ABCMeta):
    def __init__(self, path: str):
        self.__path__ = path

    @abstractmethod
    def load(self, name: str):
        pass


class SpriteLoader(Loader):
    def __init__(self):
        super().__init__("./assets/sprites/")

    def load(self, sprite: str) -> pygame.Surface:
        return pygame.image.load(self.__path__ + sprite)


class SoundLoader(Loader):
    def __init__(self):
        super().__init__("./assets/musics/")

    def load(self, music: str) -> pygame.mixer.Sound:
        return pygame.mixer.Sound(self.__path__ + music)


class LevelLoader(Loader):
    def __init__(self):
        super().__init__("./levels/")

    def load(self, level: str) -> List[str]:
        with open(self.__path__ + level, "r") as level:
            return [line.strip() for line in level]


class FontLoader(Loader):
    def __init__(self):
        super().__init__("./assets/fonts/")

    def load(self, font: str, size: int = 18) -> pygame.font.Font:
        return pygame.font.Font(self.__path__ + font, size)


sprite_loader = SpriteLoader()
sound_loader = SoundLoader()
level_loader = LevelLoader()
font_loader = FontLoader()
