from typing import Generic, Iterable, Iterator, List, TypeVar, Union
from pygame import sprite
from .types import DrawableLifecycleMethods
from .game_object import *


TGT = TypeVar("TGT", bound='GameObject')


class Group(Generic[TGT], sprite.Group, DrawableLifecycleMethods):
    """
    Надстройка над группой из библиотеки

    Нужна, чтобы возвращать типизированные объекты
    """

    def __init__(self, *sprites: TGT) -> None:
        Generic[TGT].__init__(self, (None, None))
        DrawableLifecycleMethods.__init__(self)
        sprite.Group.__init__(self, *sprites)

    def init(self, *args, **kwargs):
        for sprite in self.sprites():
            sprite.init(*args, **kwargs)
        return super().init(*args, **kwargs)

    def activate(self, *args, **kwargs):
        for sprite in self.sprites():
            if hasattr(sprite, 'activate'):
                sprite.activate(*args, **kwargs)

        return super().activate(*args, **kwargs)

    def sprites(self) -> List[TGT]:
        return super().sprites()

    def add(self, *sprites: Union[TGT, 'Group[TGT]', Iterable[Union[TGT, 'Group[TGT]']]]) -> None:
        return super().add(*sprites)

    def remove(self, *sprites: TGT) -> None:
        return super().remove(*sprites)

    def has(self, *sprites: TGT) -> bool:
        return super().has(*sprites)

    def deactivate(self, *args, **kwargs):
        for sprite in self.sprites():
            sprite.deactivate(*args, **kwargs)
        return super().deactivate(*args, **kwargs)

    def kill(self, *args, **kwargs):
        for sprite in self.sprites():
            sprite.kill(*args, **kwargs)
        return DrawableLifecycleMethods.kill(self, *args, **kwargs)

    def __iter__(self) -> Iterator[TGT]:
        return super().__iter__()
