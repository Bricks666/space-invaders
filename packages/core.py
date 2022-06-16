from abc import ABC,  abstractmethod
from typing import Dict, Final, Generic, Optional, TypeVar
from pygame import Surface, sprite, mixer


sprites = sprite.Group()
collidable = sprite.Group()


class Sprite(sprite.Sprite, ABC):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        sprites.add(self)


class Collidable(Sprite):
    __collidable__: Final[sprite.Group]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        collidable.add(self)
        self.__collidable__ = collidable

    @abstractmethod
    def __collide__(self) -> bool:
        return False


class Scene(ABC):
    __screen__: Surface
    __all_sprites__: sprite.Group
    __musics__: Dict[str, mixer.Sound]

    def __init__(self, screen: Surface) -> None:
        self.__all_sprites__ = sprite.Group()
        self.__screen__ = screen

    @abstractmethod
    def draw(self) -> None:
        self.__all_sprites__.draw(self.__screen__)

    @abstractmethod
    def update(self) -> None:
        self.__all_sprites__.update()

    @abstractmethod
    def select(self) -> None:
        self.__all_sprites__ = get_all_sprites()

    @abstractmethod
    def unselect(self) -> None:
        reset_sprites()


MT = TypeVar("MT")


class Machine(Generic[MT]):
    __screen__: Surface
    __active_scene__: Optional[Scene]
    __scenes__: Dict[MT, Scene]
    __active_scene_id__: Optional[MT]

    def __init__(self, screen: Surface):
        self.__screen__ = screen
        self.__active_scene__ = None
        self.__active_scene_id__ = None
        self.__scenes__ = dict()

    def change_scene(self, scene_id: MT, ) -> None:
        if self.__active_scene__:
            self.__active_scene__.unselect()

        self.__active_scene__ = self.__scenes__.get(scene_id)
        self.__active_scene_id__ = scene_id
        self.__active_scene__.select()

    def draw(self) -> None:
        if self.__active_scene__:
            self.__active_scene__.draw()

    def update(self) -> None:
        if self.__active_scene__:
            self.__active_scene__.update()

    def restart(self) -> None:
        pass

    def on(self,  start_scene: Optional[MT] = None) -> None:
        if start_scene:
            self.change_scene(start_scene)

    def off(self) -> None:
        if self.__active_scene__:
            self.__active_scene__.unselect()


def get_all_sprites() -> sprite.Group:
    return sprites


def get_all_sprites_by_class(cls: object) -> sprite.Group:
    cls_sprites = sprite.Group()
    for s in sprites:
        if isinstance(s, cls):
            cls_sprites.add(s)
    """
      Сделать так, чтобы возвращаемые из метода коллекции тоже сохранялись на уровне файла
      И потом очищались при вызове метода reset_sprites
    """
    return cls_sprites


def reset_sprites() -> None:
    """
    TODO: Переработать затирку
    """
    sprites.empty()
    collidable.empty()
