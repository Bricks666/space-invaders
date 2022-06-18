from typing import Callable, Dict, Literal, Union
from typing_extensions import Self
from components.text import Text, _FontSizes

_THandler = Callable[[Self], None]

_THadlerNames = Literal["on_click", "on_hover", "on_leave"]
_THandlers = Dict[_THadlerNames, _THandler]


class Button(Text):
    on_click: _THandler
    on_hover: _THandler
    on_leave: _THandler

    def __init__(self, message: str, x: float, y: float, handlers: _THandlers, size: _FontSizes = "normal") -> None:
        super().__init__(message, x, y, size)
        self.on_click = handlers.get("on_click")
        self.on_hover = handlers.get("on_hover")
        self.on_leave = handlers.get("on_leave")

    def update(self, message_data: Dict[str, Union[str, int, float]] = {}) -> None:
        return super().update(message_data)
