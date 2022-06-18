from pygame import KEYDOWN, K_r, event, key
from packages.core import Screen
from packages.events import CustomEventsTypes, create_event_params, emit_event
from screens.end.end_phrases import EndPhrases


class End(Screen):
    def activate(self, *args, **kwargs) -> None:
        self.__parts__.append(EndPhrases(self.__screen__))
        return super().activate(*args, **kwargs)

    def __control_events__(self) -> None:
        for evt in event.get(KEYDOWN):
            keys = key.get_pressed()
            if keys[K_r]:
                evt = event.Event(
                    CustomEventsTypes.CHANGE_SCREEN.value, create_event_params(screen="level"))
                emit_event(evt)
