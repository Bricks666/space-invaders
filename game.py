import sys
from typing import Dict
import pygame
from consts.main import FPS
from scenes.levels_machine import LevelsMachine
from entities.aside import Aside
from stores.level import LevelStore, Levels
from stores.lives import LivesStore
from packages.inject import Inject
from stores.scores import ScoresStore
from utils.load_font import load_font
from utils.load_music import load_music
from database.db import DB


@Inject(LevelStore, "__levels__")
@Inject(ScoresStore, "__scores__")
@Inject(LivesStore, "__lives__")
@Inject(DB, "__db__")
class Game:
    __injected__: Dict
    __levels__: LevelStore
    __scores__: ScoresStore
    __lives__: LivesStore
    __db__: DB

    def __init__(self, screen: pygame.Surface) -> None:
        self.__screen__ = screen
        self.__levels_machine__ = LevelsMachine(screen)
        self.__aside__ = Aside(screen)
        self.__running__ = False
        self.__levels__ = self.__injected__.get("__levels__")
        self.__scores__ = self.__injected__.get("__scores__")
        self.__lives__ = self.__injected__.get("__lives__")
        self.__db__ = self.__injected__.get("__db__")

    def start(self):
        self.__clock__ = pygame.time.Clock()
        self.__running__ = True
        while self.__running__:
            self.__screen__.fill((0, 0, 0))
            self.__levels_machine__.update()
            self.__levels_machine__.draw()
            self.__aside__.draw()
            self.__control_events__()
            pygame.display.update()
            self.__clock__.tick(FPS)

    def init(self) -> None:
        pygame.display.set_caption("Space invaders")
        pygame.mixer.init()
        pygame.font.init()
        load_music()
        load_font()
        self.__set_level__()

    def restart(self) -> None:
        self.__running__ = False
        self.__save_score__()
        self.__lives__.reset()
        self.__set_level__()
        self.start()

    def quite(self) -> None:
        self.__save_score__()
        self.__db__.disconnect()
        pygame.quit()
        sys.exit(0)

    def __set_level__(self) -> None:
        self.__levels_machine__.change_level(self.__levels__.get_level())

    def __save_score__(self) -> None:
        score = self.__scores__.get_scores()
        self.__db__.scores_table.add_score(score)
        self.__scores__.reset_score()

    def __control_events__(self) -> None:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.quite()
                case pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_1]:
                        self.__levels__.set_level(Levels.LEVEL1)
                        self.restart()
                    if keys[pygame.K_2]:
                        self.__levels__.set_level(Levels.LEVEL2)
                        self.restart()
                    if keys[pygame.K_r]:
                        self.restart()
