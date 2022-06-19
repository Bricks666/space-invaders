from pygame import KEYDOWN, K_l, Surface,  event, key
from components import Header
from consts.main import GAME_NAME
from packages.core import Screen
from packages.events import CustomEventsTypes, custom_event, emit_event
from screens.menu.navigation import Navigation


class Menu(Screen):
    def __init__(self, screen: Surface) -> None:
        super().__init__(screen)
        self.__musics__.get("game_start").set_volume(0.05)

    def activate(self, *args, **kwargs) -> None:
        self.__musics__.get("game_start").play(-1)
        self.__parts__.append(Header(self.__screen__, GAME_NAME))
        self.__parts__.append(Navigation(self.__screen__))
        return super().activate(*args, **kwargs)

    def inactivate(self, *args, **kwargs) -> None:
        self.__musics__.get("game_start").stop()
        return super().inactivate(*args, **kwargs)

    def __control_events__(self) -> None:
        for evt in event.get(KEYDOWN):
            if evt.type == KEYDOWN:
                keys = key.get_pressed()
                if keys[K_l]:
                    evt = custom_event(
                        CustomEventsTypes.CHANGE_SCREEN, screen="levels")
                    emit_event(evt)
