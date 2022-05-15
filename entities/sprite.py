from typing import Dict
from stores.main import inject
import pygame
from stores.level import levels


@inject(levels, "__levels__")
class Sprite(pygame.sprite.Sprite):
    __injected__: Dict

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__injected__.get("__levels__", levels).get_all_sprites().add(self)
