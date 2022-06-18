import pygame
from consts import HEIGHT, WIDTH
from database import DB
from game import Game
from stores.cache import Cache
from stores.level import LevelStore
from stores.lives import LivesStore
from stores.scores import ScoresStore
import pygame.examples.aliens

from utils.load_font import load_font


def main():
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()

    DB()
    ScoresStore()
    LevelStore()
    LivesStore()
    Cache()
    """
    Чтобы injectable сущности были доступны для внедрения
    Их нужно создать
    """
    load_font()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game = Game(screen)
    game.init()
    game.start()


if __name__ == "__main__":
    main()
