from packages.core import Screen
from .rules_header import RulesHeader
from .rules_list import RulesList


class Rules(Screen):
    """
    Экран управления
    """

    def activate(self, *args, **kwargs) -> None:
        self.__parts__.append(RulesHeader(self.__screen__, "Управление"))
        self.__parts__.append(RulesList(self.__screen__))
        """
        Части добавляются в активации,
        потому что спрайты частей очищаются при дезактивации
        и их нужно при активации заново создавать, создавая части
        """
        return super().activate(*args, **kwargs)
