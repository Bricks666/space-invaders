import sys
from typing import Dict
from consts import FPS, GAME_NAME
from consts.colors import BG_COLOR
from packages.events import CustomEventsTypes
from packages.inject import Injector
from database import DB
from screens import ScreensMachine
from utils.loaders import sprite_loader
from pygame import QUIT, event, Surface, time, display, font, quit


@Injector.inject(DB, "__db__")
class Game:
    """
    Основной объект игры
    Занимает поверхностным менеджментом игровых процессов
    """
    __db__: DB
    __screens_machine__: ScreensMachine

    def __init__(self, screen: Surface) -> None:
        self.__screen__ = screen
        self.__screens_machine__ = ScreensMachine(self.__screen__)

    def start(self):
        clock = time.Clock()
        while True:
            self.__screen__.fill(BG_COLOR)
            self.__screens_machine__.update()
            self.__screens_machine__.draw()
            self.__control_events__()
            display.update()
            clock.tick(FPS)

    def init(self) -> None:
        display.set_caption(GAME_NAME)
        display.set_icon(sprite_loader.load("enemy.png"))

        self.__db__.init()
        self.__screens_machine__.activate("menu")

    def quite(self) -> None:
        self.__screens_machine__.deactivate()
        self.__db__.disconnect()
        font.quit()
        quit()
        sys.exit(0)

    def __control_events__(self) -> None:
        for evt in event.get():
            if evt.type == QUIT:
                self.quite()
            elif evt.type == CustomEventsTypes.CHANGE_SCREEN.value:
                self.__screens_machine__.change_state(
                    evt.screen, *evt.args)
