from typing import Dict, List
from pygame import mixer, Surface, sprite, transform
from consts import LEVEL_HEIGHT, SCREEN_MARGIN, BulletType
from packages.core import Collidable


class Bullet(Collidable):
    """
    Базовый класс для пули
    """
    __musics__: Dict[str, mixer.Sound] = {}
    """
    Звуки пули
    """
    __velocity__: float
    """
    Скорость пули
    """

    def __init__(self, image: Surface, x: float, y: float, velocity: float, groups: List[sprite.Group]) -> None:
        super().__init__(*groups)
        self.__musics__.get("shoot").set_volume(0.1)
        self.__musics__.get("shoot").play()
        self.__velocity__ = velocity
        """
        По типу пули определяется ее направление
        Если она выпущена Врагом, то направление положительное, так как Y должен увеличиваться
        Если она выпушена Игроком, то направление отрицательное, так как Y должен уменьшаться
        """
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self) -> None:
        if self.__collide__():
            """
            Если произошло столкновение, то нужно уничтожить пулю
            """
            self.kill()
            return

        if self.__is_out_of_screen__():
            """
            Нужно уничтожать пулю, если она покинула предел уровня,
            чтобы оптимизировать игру количество объектов в кадре
            """
            self.kill()
            return
        self.rect.move_ip(0, self.__velocity__)

    def __is_out_of_screen__(self) -> bool:
        """
        Метод для проверки, находится ли в пределах уровня
        """
        return self.rect.y <= SCREEN_MARGIN or self.rect.y >= LEVEL_HEIGHT + SCREEN_MARGIN
