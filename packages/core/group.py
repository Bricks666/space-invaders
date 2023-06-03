from typing import Generic, Iterable, Iterator, List, TypeVar, Union, Set, Self
from .types import DrawableLifecycleMethods
from .game_object import GameObject


TGT = TypeVar("TGT", bound='GameObject')


class Group(Generic[TGT], DrawableLifecycleMethods):
    """
    Надстройка над группой из библиотеки

    Нужна, чтобы возвращать типизированные объекты
    """

    _objects: Set[TGT]

    def __init__(self, *objects: TGT) -> None:
        Generic[TGT].__init__(self, (None, None))
        DrawableLifecycleMethods.__init__(self)
        self._objects = set()

        self.add(*objects)

    def init(self, *args, **kwargs):
        for object in self.objects():
            object.init(*args, **kwargs)
        return super().init(*args, **kwargs)

    def activate(self, *args, **kwargs):
        for object in self.objects():
            object.activate(*args, **kwargs)

        return super().activate(*args, **kwargs)

    def update(self, *args, **kwargs) -> None:
        for object in self._objects:
            object.update(*args, **kwargs)

    def draw(self, *args, **kwargs) -> None:
        for object in self._objects:
            object.draw(*args, **kwargs)

    def deactivate(self, *args, **kwargs):
        for object in self.objects():
            object.deactivate(*args, **kwargs)
        return super().deactivate(*args, **kwargs)

    def kill(self, *args, **kwargs):
        for object in self.objects():
            object.kill(*args, **kwargs)
        return DrawableLifecycleMethods.kill(self, *args, **kwargs)

    def objects(self) -> List[TGT]:
        return list(self._objects)

    def add(self, *objects: Union[TGT, 'Group[TGT]', Iterable[Union[TGT, 'Group[TGT]']]]) -> Self:
        for object in objects:
            if isinstance(object, GameObject) and not self.has(object):
                self._add(object)
                continue
            self.add(*object)
        return self

    def remove(self, *objects: Union[TGT, 'Group[TGT]', Iterable[Union[TGT, 'Group[TGT]']]]) -> Self:
        for object in objects:
            if isinstance(object, GameObject) and self.has(object):
                self._remove(object)
                continue
            self.remove(*object)
        return self

    def has(self, *objects: TGT) -> bool:
        if not len(objects):
            return False

        for object in objects:
            if object not in self._objects:
                return False

        return True

    def _add(self, object: TGT) -> Self:
        self._objects.add(object)
        return self

    def _remove(self, object: TGT) -> Self:
        self._objects.remove(object)
        return self

    def __contains__(self, object: TGT) -> None:
        return self.has(object)

    def __iter__(self) -> Iterator[TGT]:
        return iter(self.objects())
