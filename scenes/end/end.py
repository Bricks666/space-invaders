from pygame import Surface
from packages.core import Screen
from scenes.end.end_phrases import EndPhrases


class End(Screen):
    def __init__(self, screen: Surface) -> None:
        super().__init__(screen)
        self.__parts__.append(EndPhrases(screen))
