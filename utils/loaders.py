from abc import ABC, abstractmethod
from typing import Final, Generic, List, TypeVar
from pygame import Surface, image
from pygame.mixer import Sound
from pygame.font import Font


T = TypeVar("T")


class Loader(ABC, Generic[T]):
    """
    Абстрактный загрузчик
    """
    __path__: Final[str]
    """
    Путь до директории с материалами
    """

    def __init__(self, path: str) -> None:
        self.__path__ = path

    @abstractmethod
    def load(self, name: str) -> T:
        """
        Метод загрузки

        Должен быть реализован у потоков
        """
        pass


class SpriteLoader(Loader[Surface]):
    """
    Загрузчик изображений
    """

    def __init__(self, path: str = "./assets/sprites/"):
        super().__init__(path)

    def load(self, sprite: str):
        return image.load(self.__path__ + sprite)


class SoundLoader(Loader[Sound]):
    """
    Загрузчик звуков
    """

    def __init__(self, path: str = "./assets/musics/"):
        super().__init__(path)

    def load(self, music: str):
        return Sound(self.__path__ + music)


class LevelLoader(Loader[List[str]]):
    """
    Загрузчик уровней
    """

    def __init__(self, path: str = "./levels/"):
        super().__init__(path)

    def load(self, level: str):
        with open(self.__path__ + level, "r") as level:
            return [line.strip() for line in level]


class FontLoader(Loader[Font]):
    """
    Загрузчик шрифтов
    """

    def __init__(self, path: str = "./assets/fonts/"):
        super().__init__(path)

    def load(self, font: str, size: int = 14):
        return Font(self.__path__ + font, size)


sprite_loader = SpriteLoader()
sound_loader = SoundLoader()
level_loader = LevelLoader()
font_loader = FontLoader()
