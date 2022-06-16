import sys
from typing import Dict
import pygame
from consts import FPS, GAME_NAME
from consts.colors import BG_COLOR
from packages.events import CustomEventsTypes
from entities.aside import Aside
from packages.inject import Inject
from database import DB
from scenes.scene_machine import ScenesMachine
from utils.load_font import load_font
from utils.load_music import load_music
from utils.loaders import sprite_loader


@Inject(DB, "__db__")
class Game:
    __injected__: Dict[str, object]
    __db__: DB
    __scenes_machine__: ScenesMachine

    def __init__(self, screen: pygame.Surface) -> None:
        self.__screen__ = screen

        self.__scenes_machine__ = ScenesMachine(screen)
        # self.__aside__ = Aside(screen)

        self.__db__ = self.__injected__.get("__db__")

    def start(self):
        clock = pygame.time.Clock()
        while True:
            self.__screen__.fill(BG_COLOR)
            self.__scenes_machine__.update()
            self.__scenes_machine__.draw()
            # self.__aside__.draw()
            self.__control_events__()
            pygame.display.update()
            clock.tick(FPS)

    def init(self) -> None:
        pygame.display.set_caption(GAME_NAME)
        pygame.display.set_icon(sprite_loader.load("enemy.png"))

        load_music()
        load_font()

        self.__db__.init()
        self.__scenes_machine__.on("level")

    def quite(self) -> None:
        self.__scenes_machine__.off()
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
                    if keys[pygame.K_r]:
                        self.__scenes_machine__.restart()
                        self.start()
                    elif keys[pygame.K_m]:
                        self.__scenes_machine__.change_scene("menu")
                    elif keys[pygame.K_l]:
                        self.__scenes_machine__.change_scene("level")
