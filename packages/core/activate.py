from abc import ABC, abstractmethod


class Activate(ABC):
    """ Вынести в отдельный класс и сделать родителем для Screen, ScreenPart, StateMachine """
    __is_active__: bool

    @abstractmethod
    def activate(self, *args, **kwargs) -> None:
        pass

    @abstractmethod
    def inactivate(self, *args, **kwargs) -> None:
        pass
