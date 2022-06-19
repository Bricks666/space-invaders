from typing import Dict
from pygame import Rect, Surface
from components.header import Header
from consts.sizes import SCREEN_MARGIN, WIDTH
from packages.inject import Injector
from stores.level import LevelStore


@Injector.inject(LevelStore, "__level__")
class EndHeader(Header):
    __injected__: Dict[str, object]
    __level__: LevelStore

    def __init__(self, screen: Surface) -> None:
        super().__init__(screen, "Уровень {level_name}")
        self.rect = Rect(SCREEN_MARGIN, SCREEN_MARGIN,
                         WIDTH - SCREEN_MARGIN * 2, SCREEN_MARGIN)

        self.__level__ = self.__injected__.get("__level__")

    def update(self, *args) -> None:
        data = {
            "level_name": self.__level__.get_current_level().level_name
        }
        return super().update(data, *args)
