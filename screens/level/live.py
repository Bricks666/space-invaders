from pygame import transform
from consts import SPRITE_SIZE
from packages.core.game_object import GameObject


class Live(GameObject):
    """
    Изображение жизни на сайдбаре
    """

    def __init__(self, x: float, y: float) -> None:
        super().__init__()
        # self.image = transform.scale(self.__images__.get(
        #     "hero"), (SPRITE_SIZE * 0.8, SPRITE_SIZE * 0.8))
        """
        В __images__ есть данный спрайт так как при загрузке
        все изображения попадают в общий общий пул
        """
        # self.rect = self.image.get_rect()
        # self.rect.x = x
        # self.rect.y = y
