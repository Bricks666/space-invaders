from packages.core import Screen
from screens.end.end_phrases import EndPhrases
from screens.end.end_header import EndHeader


class End(Screen):
    def activate(self, *args, **kwargs) -> None:
        self.__parts__.append(EndPhrases(self.__screen__))
        self.__parts__.append(EndHeader(self.__screen__))
        return super().activate(*args, **kwargs)
