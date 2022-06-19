from pygame import Surface
from components import Header, Button
from packages.events import CustomEventsTypes, custom_event, emit_event


class LevelHeader(Header):
    """
    Заголовок экрана выбора уровня
    """

    def __init__(self, screen: Surface) -> None:
        super().__init__(screen, "Уровни")

    def __create_header__(self) -> None:
        menu_button = Button("Меню", 0, 0, self.__on_click__, "small")

        menu_button.rect.center = self.rect.center
        menu_button.rect.x = self.rect.x

        self.__all_sprites__.add(menu_button)
        super().__create_header__()

    def __on_click__(self) -> None:
        evt = custom_event(CustomEventsTypes.CHANGE_SCREEN, screen="menu")
        emit_event(evt)
