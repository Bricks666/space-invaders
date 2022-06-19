from abc import ABC, abstractmethod


class Activate(ABC):
    """
    Абстрактный класс активируемой сущности

    Определяет интерфейс взаимодействия с такой сущностью
    """
    @abstractmethod
    def activate(self, *args, **kwargs) -> None:
        """
        Метод активации сущности
        """
        pass

    @abstractmethod
    def inactivate(self, *args, **kwargs) -> None:
        """
        Метод дезактивации сущности
        """
        pass
