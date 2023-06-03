from packages.core.views import Sprite
from pygame import transform, image
from consts import SPRITE_SIZE


class EnemyView(Sprite):
    def __init__(self, x=0, y=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image = transform.scale(
            image.load('./assets/sprites/enemy.png'), (SPRITE_SIZE * 0.7, SPRITE_SIZE * 0.7))
        """
        Масштабирование нужно, чтобы хитбокс не занимал все пространство спрайта
        и было место между врагами
        """
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
