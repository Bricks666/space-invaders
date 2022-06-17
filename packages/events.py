from enum import Enum
from typing import final
from pygame import event, USEREVENT


@final
class CustomEventsTypes(Enum):
    RESTART = USEREVENT + 1
    END = USEREVENT + 2


def emit_event(evt: event.Event) -> None:
    event.post(evt)
