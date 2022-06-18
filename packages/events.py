from enum import Enum
from typing import final
from pygame import event, USEREVENT


@final
class CustomEventsTypes(Enum):
    CHANGE_SCREEN = USEREVENT + 1
    RESTART = USEREVENT + 2

def emit_event(evt: event.Event) -> None:
    event.post(evt)


def custom_event(type: CustomEventsTypes, *args, **kwargs) -> event.Event:
    kwargs.update([["args", args]])
    return event.Event(type.value, kwargs)
