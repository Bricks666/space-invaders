from enum import Enum
from typing import Any, Dict, final
from pygame import event, USEREVENT


@final
class CustomEventsTypes(Enum):
    RESTART = USEREVENT + 1
    CHANGE_SCREEN = USEREVENT + 2
    END = USEREVENT + 3


def emit_event(evt: event.Event) -> None:
    event.post(evt)


def create_event_params(**kwargs) -> Dict[str, Any]:
    evt_args = dict(kwargs)
    if not evt_args.get("args"):
        evt_args.update([["args", tuple()]])

    return evt_args
