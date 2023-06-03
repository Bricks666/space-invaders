from pygame import Rect, Surface, sprite
from packages.core.game_object import Group
from packages.core.types import DrawableLifecycleMethods
from packages.core.script import Scriptable


class ScreenPart(Scriptable, DrawableLifecycleMethods):
    """
    Абстрактный класс описывающий кусок текущего экрана
    """
    __all_sprites__: Group[sprite.Sprite]
    """
    Все спрайты в данной части
    """
    __screen__: Surface
    """
    Экран, требуется для метода draw
    """
    rect: Rect
    """
    Область, занимаемая частью
    """

    def __init__(self, screen: Surface, rect: Rect) -> None:
        Scriptable.__init__(self)
        DrawableLifecycleMethods.__init__(self)
        self.__all_sprites__ = Group[sprite.Sprite]()
        self.__screen__ = screen
        self.rect = rect

    def update(self, *args) -> None:
        """
        Метод для обновления спрайтов текущей части
        """
        self.__all_sprites__.update(*args)

    def draw(self, *args) -> None:
        """
        Метод для отрисовки спрайтов текущей части
        """
        self.__all_sprites__.draw(self.__screen__, *args)

    def activate(self, *args, **kwargs) -> None:
        self.__all_sprites__.activate()
        return super().activate(*args, **kwargs)

    def deactivate(self, *args, **kwargs) -> None:
        self.__all_sprites__.deactivate()
        """
        Очистка сцены после ее дезактивации
        """
        return super().deactivate(*args, **kwargs)
