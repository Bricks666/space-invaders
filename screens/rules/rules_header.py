from components import Header, Button
from packages.events import custom_event, CustomEventsTypes, emit_event


class RulesHeader(Header):
    def __create_header__(self) -> None:

        menu = Button("Меню", 0, 0, self.__on_click__, "small")
        menu.rect.center = self.rect.center
        menu.rect.x = self.rect.x
        self.__all_sprites__.add(menu)
        return super().__create_header__()

    def __on_click__(self) -> None:
        evt = custom_event(CustomEventsTypes.CHANGE_SCREEN, screen="menu")
        emit_event(evt)
