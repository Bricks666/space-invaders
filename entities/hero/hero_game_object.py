from time import time
from typing import List, Tuple
from pygame import sprite
from consts import FIRE_COOLDOWN
from packages.core import Entity, Direction
from stores.lives import LivesStore
from packages.inject import Injector
from packages.core.scripts import attach_scripts
from .hero_script import HeroScript


@attach_scripts(HeroScript)
class Hero(Entity):
    """
    Класс игрока
    """

    def __init__(self, x: float, y: float, groups: List[sprite.Group]) -> None:
        super().__init__(*groups)
        self.image = self.__images__.get("hero")
        self.__musics__.get("explosion").set_volume(0.2)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y