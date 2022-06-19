from typing import Generic, Iterable, Iterator, List, TypeVar, Union
from pygame import sprite


TGT = TypeVar("TGT", bound=sprite.Sprite)


class Group(Generic[TGT], sprite.Group):
    """
    Надстройка над группой из библиотеки

    Нужна, чтобы возвращать типизированные объекты
    """

    def __init__(self, *sprites: TGT) -> None:
        super().__init__(*sprites)

    def sprites(self) -> List[TGT]:
        return super().sprites()

    def add(self, *sprites: Union[TGT, 'Group[TGT]', Iterable[Union[TGT, 'Group[TGT]']]]) -> None:
        return super().add(*sprites)

    def remove(self, *sprites: TGT) -> None:
        return super().remove(*sprites)

    def has(self, *sprites: TGT) -> bool:
        return super().has(*sprites)

    def __iter__(self) -> Iterator[TGT]:
        return super().__iter__()
