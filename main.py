import pygame
from consts.main import HEIGHT, WIDTH
from game import Game


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game = Game(screen)
    game.init()
    game.start()


if __name__ == "__main__":
    main()
