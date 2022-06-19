from typing import Callable, Dict, Union
from components.text import Text, _FontSizes
from consts.colors import BORDER_COLOR, TEXT_COLOR
from pygame import SYSTEM_CURSOR_CROSSHAIR, SYSTEM_CURSOR_HAND, mouse, cursors, mixer, time

_THandler = Callable[['Button'], None]


class Button(Text):
    __hovering__: bool = False
    __sounds__: Dict[str, mixer.Sound] = {}
    on_click: _THandler

    def __init__(self, message: str, x: float, y: float, on_click: _THandler, size: _FontSizes = "normal") -> None:
        super().__init__(message, x, y, size)
        self.on_click = on_click

    def update(self, message_data: Dict[str, Union[str, int, float]] = {}) -> None:
        mouse_position = mouse.get_pos()
        if self.rect.collidepoint(mouse_position):
            if not self.__hovering__:
                self.__hovering__ = True
                self.on_hover()

            pressed = mouse.get_pressed()
            if pressed[0]:
                self.__on_click__()
                self.on_leave()

        elif self.__hovering__:
            self.__hovering__ = False
            self.on_leave()

        return super().update(message_data)

    def on_hover(self) -> None:
        self.change_color(BORDER_COLOR)
        mouse.set_cursor(SYSTEM_CURSOR_HAND)

    def on_leave(self) -> None:
        self.change_color(TEXT_COLOR)
        mouse.set_cursor(cursors.tri_left)

    @classmethod
    def set_sound(cls, name: str, sound: mixer.Sound) -> None:
        cls.__sounds__.update([[name, sound]])

    def __on_click__(self) -> None:
        self.__sounds__.get("click").play(fade_ms=300, maxtime=300)
        time.wait(300)
        self.on_click()
