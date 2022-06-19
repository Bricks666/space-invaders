from pygame import Rect, Surface, event
import pygame
from components.button import Button
from components.text import Text
from consts.main import GAME_NAME
from consts.sizes import CONTENT_HEIGHT, CONTENT_WIDTH, SCREEN_MARGIN, SPRITE_SIZE
from packages.core import ScreenPart
from packages.events import CustomEventsTypes, custom_event, emit_event


class Navigation(ScreenPart):
    def __init__(self, screen: Surface) -> None:
        rect = Rect(SCREEN_MARGIN, SCREEN_MARGIN,
                    CONTENT_WIDTH, CONTENT_HEIGHT)
        super().__init__(screen, rect)

    def activate(self, *args, **kwargs) -> None:
        self.__create_text__()
        return super().activate(*args, **kwargs)

    def inactivate(self, *args, **kwargs) -> None:
        return super().inactivate(*args, **kwargs)

    def __create_text__(self) -> None:

        play = Button(
            "Играть", 0, 0,
            lambda: emit_event(custom_event(
                CustomEventsTypes.CHANGE_SCREEN, screen="levels"))
        )

        rules = Button(
            "Управление", 0, 0,
            lambda: emit_event(custom_event(
                CustomEventsTypes.CHANGE_SCREEN, screen="rules"))
        )
        exit = Button(
            "Выйти", 0, 0, lambda: emit_event(event.Event(pygame.QUIT)))

        play.rect.center =  \
            exit.rect.center = rules.rect.center = self.rect.center
        play.rect.move_ip(0, -SPRITE_SIZE * 0.5)
        exit.rect.move_ip(0, SPRITE_SIZE * 0.5)

        self.__all_sprites__.add(
            play, exit, rules)
