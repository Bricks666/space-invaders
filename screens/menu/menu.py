from pygame import KEYDOWN, K_l,  event, key
from packages.core import Screen
from packages.events import CustomEventsTypes, custom_event, emit_event
from screens.menu.menu_part import MenuPart


class Menu(Screen):
    def activate(self, *args, **kwargs) -> None:
        self.__parts__.append(MenuPart(self.__screen__))
        return super().activate(*args, **kwargs)

    def __control_events__(self) -> None:
        for evt in event.get(KEYDOWN):
            if evt.type == KEYDOWN:
                keys = key.get_pressed()
                if keys[K_l]:
                    evt = custom_event(
                        CustomEventsTypes.CHANGE_SCREEN, screen="levels")
                    emit_event(evt)
