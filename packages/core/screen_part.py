from pygame import Rect, Surface, sprite
from .activate import Activate
from .group import Group


class ScreenPart(Activate):
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
        return super().activate(*args, **kwargs)

    def inactivate(self, *args, **kwargs) -> None:
        self.__all_sprites__.empty()
        """
        Очистка сцены после ее дезактивации
        """
        return super().inactivate(*args, **kwargs)
