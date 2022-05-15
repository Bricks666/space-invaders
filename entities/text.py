import pygame


class Text:
    FONT: pygame.font.Font

    def generate(self, message: str, color: pygame.Color = pygame.Color(125, 125, 125)) -> pygame.Surface:
        return Text.FONT.render(message, True, color)
