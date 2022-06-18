from pygame import Surface, sprite
from packages.core.activate import Activate
from packages.core.group import Group


class ScreenPart(Activate):
    __all_sprites__: Group[sprite.Sprite]
    __screen__: Surface

    def __init__(self, screen: Surface) -> None:
        self.__all_sprites__ = Group[sprite.Sprite]()
        self.__screen__ = screen

    def update(self, *args) -> None:
        self.__all_sprites__.update(*args)

    def draw(self, *args) -> None:
        self.__all_sprites__.draw(self.__screen__, *args)

    def activate(self, *args, **kwargs) -> None:
        return super().activate(*args, **kwargs)

    def inactivate(self, *args, **kwargs) -> None:
        self.__all_sprites__.empty()
        return super().inactivate(*args, **kwargs)
