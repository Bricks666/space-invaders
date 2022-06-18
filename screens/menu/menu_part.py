from pygame import Rect, Surface, event
import pygame
from components.button import Button
from components.text import Text
from consts.main import GAME_NAME
from consts.sizes import HEIGHT, SCREEN_MARGIN, SPRITE_SIZE, WIDTH
from packages.core import ScreenPart
from packages.events import CustomEventsTypes, custom_event, emit_event


class MenuPart(ScreenPart):
    def __init__(self, screen: Surface) -> None:
        super().__init__(screen)

        self.rect = Rect(SCREEN_MARGIN, SCREEN_MARGIN,
                         WIDTH - SCREEN_MARGIN * 2, HEIGHT - SCREEN_MARGIN * 2)

    def activate(self, *args, **kwargs) -> None:
        self.__create_text__()
        return super().activate(*args, **kwargs)

    def inactivate(self, *args, **kwargs) -> None:
        return super().inactivate(*args, **kwargs)

    def __create_text__(self) -> None:
        game_name_text = Text(GAME_NAME, 0, 0, "large")

        level_text = Button(
            "Уровни", 0, 0,
            lambda: emit_event(custom_event(
                CustomEventsTypes.CHANGE_SCREEN, screen="levels"))
        )
        menu_text = Button(
            "Выйти", 0, 0, lambda: emit_event(event.Event(pygame.QUIT)))

        level_text.rect.center = game_name_text.rect.center = \
            menu_text.rect.center = self.rect.center
        game_name_text.rect.y -= SPRITE_SIZE * 5
        level_text.rect.y -= SPRITE_SIZE * 0.5

        self.__all_sprites__.add(game_name_text, level_text, menu_text)
