from typing import Dict
from pygame import Rect, Surface
from consts.sizes import SCREEN_MARGIN, WIDTH
from packages.core import ScreenPart
from components.text import Text
from packages.inject import Injector
from stores.level import LevelStore


@Injector.inject(LevelStore, "__level__")
class Header(ScreenPart):
    __injected__: Dict[str, object]
    __level__: LevelStore

    def __init__(self, screen: Surface) -> None:
        super().__init__(screen)
        self.rect = Rect(SCREEN_MARGIN, SCREEN_MARGIN,
                         WIDTH - SCREEN_MARGIN * 2, SCREEN_MARGIN)

        self.__level__ = self.__injected__.get("__level__")

    def activate(self, *args, **kwargs) -> None:
        self.__create_text__()
        return super().activate(*args, **kwargs)

    def update(self, *args) -> None:
        data = {
            "level_name": self.__level__.get_current_level().level_name
        }
        return super().update(data, *args)

    def __create_text__(self) -> None:
        level_name_text = Text("Уровень {level_name}", 0, 0)
        level_name_text.rect.center = self.rect.center
        level_name_text.rect.y = self.rect.y
        self.__all_sprites__.add(level_name_text)
