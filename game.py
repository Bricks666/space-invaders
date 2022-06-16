import sys
from typing import Dict
import pygame
from consts import FPS, GAME_NAME
from packages.events import CustomEventsTypes
from scenes.levels_machine import LevelsMachine
from entities.aside import Aside
from packages.inject import Inject
from database import DB
from utils.load_font import load_font
from utils.load_music import load_music
from utils.loaders import sprite_loader


@Inject(DB, "__db__")
class Game:
    __injected__: Dict[str, object]
    __db__: DB

    def __init__(self, screen: pygame.Surface) -> None:
        self.__screen__ = screen
        self.__levels_machine__ = LevelsMachine(screen)
        self.__aside__ = Aside(screen)
        self.__running__ = False
        self.__db__ = self.__injected__.get("__db__")

    def start(self):
        clock = pygame.time.Clock()
        self.__running__ = True
        while self.__running__:
            self.__screen__.fill((0, 0, 0))
            self.__levels_machine__.update()
            self.__levels_machine__.draw()
            self.__aside__.draw()
            self.__control_events__()
            pygame.display.update()
            clock.tick(FPS)

    def init(self) -> None:
        pygame.display.set_caption(GAME_NAME)
        pygame.display.set_icon(sprite_loader.load("enemy.png"))

        load_music()
        load_font()

        self.__db__.init()
        self.__levels_machine__.on()

    def quite(self) -> None:
        self.__levels_machine__.off()
        self.__db__.disconnect()
        pygame.font.quit()
        pygame.quit()
        sys.exit(0)

    def __control_events__(self) -> None:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.quite()
                case CustomEventsTypes.RESTART.value:
                    self.start()
                case pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    print(keys[pygame.K_r], pygame.K_r, event.key)
                    if keys[pygame.K_r]:
                        self.__levels_machine__.restart()
                        self.start()
