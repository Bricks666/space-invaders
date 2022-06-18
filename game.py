import sys
from typing import Dict
import pygame
from consts import FPS, GAME_NAME
from consts.colors import BG_COLOR
from packages.events import CustomEventsTypes
from packages.inject import Injector
from database import DB
from screens import ScreensMachine
from utils.loaders import sprite_loader


@Injector.inject(DB, "__db__")
class Game:
    """
    Основной объект игры
    Занимает поверхностным менеджментом игровых процессов
    """
    __injected__: Dict[str, object]
    __db__: DB
    __screens_machine__: ScreensMachine

    def __init__(self, screen: pygame.Surface) -> None:
        self.__screen__ = screen
        self.__screens_machine__ = ScreensMachine(screen)
        self.__db__ = self.__injected__.get("__db__")

    def start(self):
        clock = pygame.time.Clock()
        while True:
            self.__screen__.fill(BG_COLOR)
            self.__screens_machine__.update()
            self.__screens_machine__.draw()
            self.__control_events__()
            pygame.display.update()
            clock.tick(FPS)

    def init(self) -> None:
        pygame.display.set_caption(GAME_NAME)
        pygame.display.set_icon(sprite_loader.load("enemy.png"))

        self.__db__.init()
        self.__screens_machine__.activate("menu")

    def quite(self) -> None:
        self.__screens_machine__.inactivate()
        self.__db__.disconnect()
        pygame.font.quit()
        pygame.quit()
        sys.exit(0)

    def __control_events__(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quite()
            elif event.type == CustomEventsTypes.CHANGE_SCREEN.value:
                self.__screens_machine__.change_state(
                    event.screen, *event.args)
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_m]:
                    self.__screens_machine__.change_state("menu")
