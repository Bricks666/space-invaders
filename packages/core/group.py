from typing import Generic, Iterable, List, TypeVar, Union
from pygame import sprite


TGT = TypeVar("TGT", bound=sprite.Group)


class Group(Generic[TGT], sprite.Group):

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

    @staticmethod
    def get_by_class(sprites: sprite.Group, cls: TGT) -> 'Group[TGT]':
        group = Group[TGT]()

        for s in sprites:
            if isinstance(s, cls):
                group.add(s)
        return group
