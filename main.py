from pygame import init, mixer, font, display, mouse, cursors
from consts import HEIGHT, WIDTH
from game import Game
from packages.inject import Injector

from utils.load_fonts import load_fonts
from utils.load_images import load_images
from utils.load_musics import load_musics


def main():
    init()
    mixer.init()
    font.init()
    mouse.set_cursor(cursors.tri_left)

    Injector.init()

    load_fonts()
    load_images()
    load_musics()

    screen = display.set_mode((WIDTH, HEIGHT))
    game = Game(screen)
    game.init()
    game.start()


if __name__ == "__main__":
    main()
