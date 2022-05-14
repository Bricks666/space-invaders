import pygame


class Scene:
    def __init__(self, screen: pygame.Surface, sprites: pygame.sprite.Group):
        self._sprites = sprites
        self._screen = screen
        pass

    def draw(self):
        self._sprites.draw(self._screen)

    def update(self):
        self._sprites.update()
