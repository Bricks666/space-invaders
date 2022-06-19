from packages.core import Screen
from screens.rules.rules_header import RulesHeader
from screens.rules.rules_list import RulesList


class Rules(Screen):
    def activate(self, *args, **kwargs) -> None:
        self.__parts__.append(RulesHeader(self.__screen__, "Управление"))
        self.__parts__.append(RulesList(self.__screen__))
        return super().activate(*args, **kwargs)
