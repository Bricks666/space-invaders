from pygame import Rect, Surface
from consts.sizes import CONTENT_HEIGHT, CONTENT_WIDTH
from packages.core import ScreenPart
from consts import SCREEN_MARGIN
from components import Text


class RulesList(ScreenPart):
    def __init__(self, screen: Surface) -> None:
        rect = Rect(SCREEN_MARGIN, SCREEN_MARGIN * 2.5,
                    CONTENT_WIDTH, CONTENT_HEIGHT - SCREEN_MARGIN * 2.5)
        super().__init__(screen, rect)

    def activate(self, *args, **kwargs) -> None:
        self.__create_list__()
        return super().activate(*args, **kwargs)

    def __create_list__(self) -> None:
        move_left = Text("A/<- - движение влево", 0, 0)
        move_right = Text("D/-> - движение вправо", 0, 0)
        fire = Text("SPACE - стрелять", 0, 0)

        line_height = Text.get_font_height(fire) * 1.5

        move_left.rect.center = move_right.rect.center = \
            fire.rect.center = self.rect.center
        move_left.rect.move_ip(0, -line_height)
        fire.rect.move_ip(0, line_height)

        self.__all_sprites__.add(move_right, move_left, fire)
