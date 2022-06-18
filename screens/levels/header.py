from pygame import Rect, Surface
from components.button import Button
from consts.sizes import SCREEN_MARGIN, SPRITE_SIZE, WIDTH
from packages.core import ScreenPart
from components.text import Text
from packages.events import CustomEventsTypes, custom_event, emit_event


class Header(ScreenPart):
    def __init__(self, screen: Surface) -> None:
        super().__init__(screen)
        self.rect = Rect(SCREEN_MARGIN, SCREEN_MARGIN,
                         WIDTH - SCREEN_MARGIN * 2, SPRITE_SIZE)

    def activate(self, *args, **kwargs) -> None:
        self.__create_text__()
        return super().activate(*args, **kwargs)

    def __create_text__(self) -> None:
        header_text = Text("Уровни", 0, 0)

        menu_button = Button("Меню", 0, 0, lambda: emit_event(
            custom_event(CustomEventsTypes.CHANGE_SCREEN, screen="menu")), "small")

        menu_button.rect.center = header_text.rect.center = self.rect.center
        menu_button.rect.x = self.rect.x

        self.__all_sprites__.add(header_text, menu_button)
