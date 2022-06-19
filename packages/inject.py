from typing import Callable, Dict, List, TypeVar, final


T = TypeVar("T", bound=object)


@final
class Injector:
    """
    Класс обеспечивающий DI в проекте
    """
    __injectable_dict__: Dict[object, object] = {}
    """
    Нужно для хранения созданных экземпляров внедряемых объектов
    """
    __injectable_list__: List[object] = []
    """
    Список классов, которые будут внедряться
    """

    @classmethod
    def inject(cls, store_class: object, name: str) -> Callable:
        """
        Декоратор для внедрения экземпляров объектов в экземпляр класса
        """
        def inner(injectable: T) -> T:
            orig_init = injectable.__init__
            """
            Дополнение __init__, чтобы внедрить зависимость
            """

            def __init__(self: T, *args, **kwargs) -> None:
                store = cls.__injectable_dict__.get(store_class)
                if not store:
                    raise ValueError(
                        f'Store with type {store_class} is not exists')

                self.__dict__.update([[name, store]])
                """
                Добавление свойства в словарь, описывающий объект добавляет его и в сам объект
                """

                orig_init(self, *args, **kwargs)

            injectable.__init__ = __init__

            return injectable

        return inner

    @classmethod
    def injectable(cls) -> Callable:
        """
        Помечает класс как возможный для внедрения
        """
        def inner(injectable: T) -> T:
            cls.__injectable_list__.append(injectable)
            return injectable

        return inner

    @classmethod
    def init(cls) -> None:
        """
        Нужен для автоматического создания экземпляров внедряемых объектов
        """
        for injectable in cls.__injectable_list__:
            cls.__injectable_dict__.update([[injectable, injectable()]])
