from typing import Dict
from pygame import Rect, Surface
from consts.sizes import HEIGHT, SCREEN_MARGIN, SPRITE_SIZE, WIDTH
from models.level import LevelModel
from packages.events import CustomEventsTypes, custom_event, emit_event
from packages.inject import Injector
from stores.level import LevelStore
from packages.core import ScreenPart, Group
from components.button import Button


@Injector.inject(LevelStore, "__levels__")
class List(ScreenPart):
    __injected__: Dict[str, object]
    __levels__: LevelStore

    def __init__(self, screen: Surface) -> None:
        super().__init__(screen)
        self.rect = Rect(SCREEN_MARGIN * 2, SCREEN_MARGIN * 2.5,
                         WIDTH - SCREEN_MARGIN * 4, HEIGHT - SCREEN_MARGIN * 4.5)

        self.__levels__ = self.__injected__.get("__levels__")
        self.__levels__.fetch_levels()

    def activate(self, *args, **kwargs) -> None:
        levels = self.__levels__.get_levels()
        level_row_count = (WIDTH - SCREEN_MARGIN * 4) // SPRITE_SIZE
        level_sprites: Group[Button] = Group()
        for i in range(len(levels)):
            level_sprites.add(self.__create_level_button__(
                levels[i], i, level_row_count))

        self.__all_sprites__.add(level_sprites)
        return super().activate(*args, **kwargs)

    def __create_level_button__(self, level: LevelModel, i: int, level_row_count: float) -> Button:
        x = self.rect.x + i % level_row_count * SPRITE_SIZE
        y = self.rect.y + i // level_row_count * SPRITE_SIZE

        def on_click(): return emit_event(
            custom_event(CustomEventsTypes.CHANGE_SCREEN, level.level_id, screen="level"))
        return Button(str(level.level_id), x, y, on_click)
