import pygame


class Text:
    FONT: pygame.font.Font

    @classmethod
    def generate(cls, message: str, color: pygame.Color = pygame.Color(125, 125, 125)) -> pygame.Surface:
        return cls.FONT.render(message, True, color)
