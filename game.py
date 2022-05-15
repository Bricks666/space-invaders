import sys
from typing import Dict
import pygame
from consts.main import FPS
from scenes.levels_machine import LevelsMachine
from entities.aside import Aside
from stores.level import LevelStore, Levels, levels
from stores.main import inject
from utils.load_font import load_font
from utils.load_music import load_music


@inject(levels, "__levels__")
class Game:
    __injected__: Dict
    __levels__: LevelStore

    def __init__(self, screen: pygame.Surface):
        self.__screen__ = screen
        self.__levels_machine__ = LevelsMachine(screen)
        self.__aside__ = Aside(screen)
        self.__running__ = False
        self.__levels__ = self.__injected__.get("__levels__")

    def start(self):
        self.__clock__ = pygame.time.Clock()
        self.__running__ = True
        while self.__running__:
            self.__screen__.fill((0, 0, 0))
            self.__levels_machine__.update()
            self.__levels_machine__.draw()
            self.__aside__.draw()
            self.__controll_events__()
            pygame.display.update()
            self.__clock__.tick(FPS)

    def init(self):
        pygame.display.set_caption("Space invader")
        pygame.mixer.init()
        pygame.font.init()
        load_music()
        load_font()
        self.__levels_machine__.change_level(self.__levels__.get_level())

    def restart(self):
        pass

    def quite(self):
        pygame.quit()
        sys.exit(0)

    def __controll_events__(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.quite()
                case pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_1]:
                        self.__levels_machine__.change_level(Levels.LEVEL1)
                    if keys[pygame.K_2]:
                        self.__levels_machine__.change_level(Levels.LEVEL2)
