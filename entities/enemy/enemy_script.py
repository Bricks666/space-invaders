from time import time
from .enemy_game_object import *
from packages.core.scripts import Script
from packages.inject import Injector
from stores.scores import ScoresStore
from packages.core.entity import Direction
from consts import SCREEN_MARGIN, LEVEL_WIDTH


@Injector.inject(ScoresStore, "__scores__")
class EnemyScript(Script["Enemy"]):
    __scores__: ScoresStore
    """
    Хранилище очков
    """
    __move_timeout__: float = 1
    """
    Время в секундах, которое должно пройти,
    прежде чем враг сможет сдвинуться
    """
    __offset_left__: float
    __offset_right__: float
    """
    Точки, за которые враг на может перемешаться
    Чтобы не залезать на соседних врагов, и сделать ограниченность маршрута по уровню
    """

    __end__: bool
    """
    Дошел ли враг до своей точки, которую нельзя пересекать
    """

    __score__: int
    """
    Количество очков получаемых за уничтожение врага
    """
    __last_move__: float
    """
    Время в секундах с момента последнего движения
    """
    __velocity__: float

    def activate(self, *args, **kwargs):
        total_count = self._game_object._total_number
        number = self._game_object._number

        self.__offset_right__ = SPRITE_SIZE * (total_count - number)
        self.__offset_left__ = SPRITE_SIZE * number
        self.__velocity__ = SPRITE_SIZE / 4 * Direction.LEFT.value
        self.__end__ = False
        self.__last_move__ = time()
        self.__score__ = 50

    def update(self):
        self.move()
        return super().update()

    def move(self) -> None:
        current_time = time()
        if not self.__can_move__(current_time):
            return

        self.__last_move__ = current_time
        self._game_object.__musics__.get("step").play()
        if self.__end__:
            self.__change_direction__()
            self.__end__ = False
            self._game_object.rect.move_ip(0, SPRITE_SIZE / 2)
            return

        self._game_object.rect.move_ip(self.__velocity__, 0)
        self.__end__ = self.__check_end__()

    def kill(self) -> None:
        self._game_object.__musics__.get("destroy").play()
        self.__scores__.add(self.__score__)
        return super().kill()

    def __check_end__(self) -> bool:
        """
        Метод проверяет, дошел ли враг до конца
        """
        return self._game_object.rect.x <= SCREEN_MARGIN + self.__offset_left__ or \
            self._game_object.rect.x >= LEVEL_WIDTH + SCREEN_MARGIN - self.__offset_right__

    def __change_direction__(self) -> None:
        """
        Изменяет направление движения
        """
        self.__velocity__ *= -1

    def __can_move__(self, current_time: float) -> bool:
        print(self.__last_move__ + self.__move_timeout__ <= current_time)
        return self.__last_move__ + self.__move_timeout__ <= current_time
