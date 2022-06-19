from pygame import Rect, Surface
from consts.sizes import SCREEN_MARGIN, SPRITE_SIZE, WIDTH
from components import Header, Button
from packages.events import CustomEventsTypes, custom_event, emit_event


class LevelHeader(Header):
    def __init__(self, screen: Surface) -> None:
        super().__init__(screen, "Уровни")
        self.rect = Rect(SCREEN_MARGIN, SCREEN_MARGIN,
                         WIDTH - SCREEN_MARGIN * 2, SPRITE_SIZE)

    def __create_header__(self) -> None:
        menu_button = Button("Меню", 0, 0, lambda: emit_event(
            custom_event(CustomEventsTypes.CHANGE_SCREEN, screen="menu")), "small")

        menu_button.rect.center = self.rect.center
        menu_button.rect.x = self.rect.x

        self.__all_sprites__.add(menu_button)
        super().__create_header__()
