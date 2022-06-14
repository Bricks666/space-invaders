from typing import Dict
from packages.inject import Inject
import pygame
from stores.level import LevelStore


@Inject(LevelStore, "__levels__")
class Sprite(pygame.sprite.Sprite):
    __injected__: Dict

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__injected__.get("__levels__").get_all_sprites().add(self)
