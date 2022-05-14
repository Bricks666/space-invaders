import pygame


class SpriteLoader:
    PATH = "./assets/sprites/"

    @classmethod
    def load(cls, sprite: str) -> pygame.Surface:
        return pygame.image.load(cls.PATH + sprite)
