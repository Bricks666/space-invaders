import pygame
from consts.main import HEIGHT, WIDTH
from database.db import DB
from game import Game
from stores.level import LevelStore
from stores.lives import LivesStore
from stores.scores import ScoresStore


def main():
    pygame.init()
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
