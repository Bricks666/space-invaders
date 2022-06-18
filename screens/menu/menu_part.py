from pygame import Rect, Surface
from components.text import Text
from consts.main import GAME_NAME
from consts.sizes import HEIGHT, SCREEN_MARGIN, SPRITE_SIZE, WIDTH
from packages.core import ScreenPart


class MenuPart(ScreenPart):
    def __init__(self, screen: Surface) -> None:
        super().__init__(screen)

        self.rect = self.rect = Rect(SCREEN_MARGIN, SCREEN_MARGIN,
                                     WIDTH - SCREEN_MARGIN, HEIGHT - SCREEN_MARGIN)

    def activate(self, *args, **kwargs) -> None:
        self.__create_text__()
        return super().activate(*args, **kwargs)

    def inactivate(self, *args, **kwargs) -> None:
        return super().inactivate(*args, **kwargs)

    def __create_text__(self) -> None:
        game_name_text = Text(GAME_NAME, 0, 0, "large")

        level_text = Text(
            "Чтобы перейти к уровням нажмите L", 0, 0)
        menu_text = Text(
            "Чтобы вернуться в меню нажмите M", 0, 0)

        level_text.rect.center = game_name_text.rect.center = \
            menu_text.rect.center = self.rect.center
        game_name_text.rect.y -= SPRITE_SIZE * 5
        level_text.rect.y -= SPRITE_SIZE * 0.5

        self.__all_sprites__.add(game_name_text, level_text, menu_text)
