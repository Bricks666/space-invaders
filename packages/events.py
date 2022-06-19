from enum import Enum
from typing import final
from pygame import event, USEREVENT


@final
class CustomEventsTypes(Enum):
    CHANGE_SCREEN = USEREVENT + 1


def emit_event(evt: event.Event) -> None:
    """
    Небольшая надстройка над методом отправки событий

    Нужна, чтобы не импортировать event
    """
    event.post(evt)


def custom_event(type: CustomEventsTypes, *args, **kwargs) -> event.Event:
    """
    Нужен для автоматизации создания собственных событий по нужно структуре,
    так как нельзя отнаследоваться от класса event.Event
    """
    if not kwargs.get("args"):
        kwargs.update([["args", args]])
    return event.Event(type.value, kwargs)
