from pygame import Rect, Surface, sprite
from .types import DrawableLifecycleMethods
from .script import Scriptable
from .game_object import Group, GameObject


class ScreenPart(Scriptable, DrawableLifecycleMethods):
    """
    Абстрактный класс описывающий кусок текущего экрана
    """
    __objects__: Group[GameObject]
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

    def __init__(self, screen: Surface, rect: Rect, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__objects__ = Group[sprite.Sprite]()
        self.__screen__ = screen
        self.rect = rect

    def update(self, *args, **kwargs) -> None:
        """
        Метод для обновления спрайтов текущей части
        """
        Scriptable.update(self, *args, **kwargs)
        self.__objects__.update(*args, **kwargs)

    def draw(self, *args) -> None:
        """
        Метод для отрисовки спрайтов текущей части
        """
        self.__objects__.draw(self.__screen__, *args)

    def activate(self, *args, **kwargs) -> None:
        Scriptable.activate(self, *args, **kwargs)
        self.__objects__.activate()

    def deactivate(self, *args, **kwargs) -> None:
        self.__objects__.deactivate()
        """
        Очистка сцены после ее дезактивации
        """
        return super().deactivate(*args, **kwargs)
