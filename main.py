import pygame
from consts import HEIGHT, WIDTH
from database import DB
from game import Game
from stores.level import LevelStore
from stores.lives import LivesStore
from stores.scores import ScoresStore
import pygame.examples.aliens


def main():
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()

    DB()
    ScoresStore()
    LevelStore()
    LivesStore()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game = Game(screen)
    game.init()
    game.start()


if __name__ == "__main__":
    main()
