from components import Header, Button
from packages.events import custom_event, CustomEventsTypes, emit_event


class RulesHeader(Header):
    """
    Заголовок блока правил
    """

    def __create_header__(self) -> None:
        menu = Button("Меню", 0, 0, self.__on_click__, "small")
        menu.rect.center = self.rect.center
        menu.rect.x = self.rect.x
        self.__objects__.add(menu)
        return super().__create_header__()

    def __on_click__(self) -> None:
        """
        Обработчик клика на кнопку
        """
        evt = custom_event(CustomEventsTypes.CHANGE_SCREEN, screen="menu")
        emit_event(evt)
