from abc import ABCMeta, abstractmethod
from typing import Final, List
import pygame


class Loader(metaclass=ABCMeta):
    _path_: Final[str]

    def __init__(self, path: str):
        self._path_ = path

    @abstractmethod
    def load(self, name: str):
        pass


class SpriteLoader(Loader):
    def __init__(self, path: str = "./assets/sprites/"):
        super().__init__(path)

    def load(self, sprite: str) -> pygame.Surface:
        return pygame.image.load(self._path_ + sprite)


class SoundLoader(Loader):
    def __init__(self, path: str = "./assets/musics/"):
        super().__init__(path)

    def load(self, music: str) -> pygame.mixer.Sound:
        return pygame.mixer.Sound(self._path_ + music)


class LevelLoader(Loader):
    def __init__(self, path: str = "./levels/"):
        super().__init__(path)

    def load(self, level: str) -> List[str]:
        with open(self._path_ + level, "r") as level:
            return [line.strip() for line in level]


class FontLoader(Loader):
    def __init__(self, path: str = "./assets/fonts/"):
        super().__init__(path)

    def load(self, font: str, size: int = 18) -> pygame.font.Font:
        return pygame.font.Font(self._path_ + font, size)


sprite_loader = SpriteLoader()
sound_loader = SoundLoader()
level_loader = LevelLoader()
font_loader = FontLoader()
