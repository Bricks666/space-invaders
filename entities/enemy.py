from time import time
from typing import List
from pygame import Surface, mixer, transform, sprite
from consts.main import STEP
from entities.bullet import Bullet
from packages.core import Direction, Entity
from packages.inject import Injector
from stores.scores import ScoresStore
from consts import LEVEL_WIDTH, SCREEN_MARGIN, SPRITE_SIZE, BulletType


@Injector.inject(ScoresStore, "__scores__")
class Enemy(Entity):
    """
    Враг
    """
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

    def __init__(self, x: float, y: float, number: int, total_count: int, groups: List[sprite.Group], score: int = 50) -> None:
        super().__init__(*groups)
        self.image = transform.scale(
            Enemy.__images__.get("enemy"), (SPRITE_SIZE * 0.7, SPRITE_SIZE * 0.7))
        """
        Масштабирование нужно, чтобы хитбокс не занимал все пространство спрайта
        и было место между врагами
        """
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.__musics__.get('step').set_volume(0.1)
        self.__musics__.get("destroy").set_volume(0.1)

        self.__offset_right__ = SPRITE_SIZE * (total_count - number)
        self.__offset_left__ = SPRITE_SIZE * number
        self.__velocity__ = SPRITE_SIZE / 4 * Direction.LEFT.value
        self.__end__ = False
        self.__last_move__ = time()
        self.__score__ = score

    def update(self) -> None:
        if self.__collide__():
            return
        self.move()
        return super().update()

    def fire(self) -> None:
        groups = self.groups()
        groups.pop()
        """
        Нужно так как враг состоит в группе всех спрайтов сцены,
        объектов для коллизии и отдельной группы врагов
        Она самая последняя и в нее не нужно добавлять пулю
        """
        EnemyBullet(self.__images__.get("enemy_bullet"), self.rect.centerx,
                    self.rect.y + self.rect.height, groups)

    def move(self) -> None:
        current_time = time()
        if not self.__can_move__(current_time):
            return

        self.__last_move__ = current_time
        self.__musics__.get("step").play()
        if self.__end__:
            self.__change_direction__()
            self.__end__ = False
            self.rect.move_ip(0, SPRITE_SIZE / 2)
            return

        self.rect.move_ip(self.__velocity__, 0)
        self.__end__ = self.__check_end__()

    def kill(self) -> None:
        self.__musics__.get("destroy").play()
        self.__scores__.add(self.__score__)
        return super().kill()

    def __check_end__(self) -> bool:
        """
        Метод проверяет, дошел ли враг до конца
        """
        return self.rect.x <= SCREEN_MARGIN + self.__offset_left__ or self.rect.x >= LEVEL_WIDTH + SCREEN_MARGIN - self.__offset_right__

    def __change_direction__(self) -> None:
        """
        Изменяет направление движения
        """
        self.__velocity__ *= -1

    def __can_move__(self, current_time: float) -> bool:
        return self.__last_move__ + self.__move_timeout__ <= current_time

    def __collide__(self) -> bool:
        return super().__collide__()


class EnemyBullet(Bullet):
    def __init__(self, image: Surface, x: float, y: float, groups: List[sprite.Group]) -> None:
        velocity = STEP * 3 * BulletType.ENEMY.value
        super().__init__(image, x, y, velocity, groups)

    def __collide__(self) -> bool:
        for s in self.__collidable__.sprites():
            if s == self or isinstance(s, (Enemy, EnemyBullet)):
                """
                Не дает застрелить себя, другую пулю врага или врага
                """
                continue
            if sprite.collide_rect(self, s):
                s.kill()
                return True
        return False
