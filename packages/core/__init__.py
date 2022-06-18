from packages.core.collidable import *
from packages.core.machine import *
from packages.core.screen import *
from packages.core.group import *


class Activate(ABC):
    """ Вынести в отдельный класс и сделать родителем для Screen, ScreenPart, StateMachine """
    __is_active__: bool

    @abstractmethod
    def activate(self, *args, **kwargs) -> None:
        pass

    @abstractmethod
    def inactivate(self, *args, **kwargs) -> None:
        pass
