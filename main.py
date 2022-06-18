from pygame import init, mixer, font, display
from consts import HEIGHT, WIDTH
from game import Game
from packages.inject import Injector
import pygame.examples.aliens

from utils.load_font import load_font


def main():
    init()
    mixer.init()
    font.init()

    Injector.init()

    load_font()

    screen = display.set_mode((WIDTH, HEIGHT))
    game = Game(screen)
    game.init()
    game.start()


if __name__ == "__main__":
    main()
