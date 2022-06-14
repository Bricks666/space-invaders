from typing import Callable, Dict, TypeVar

T = TypeVar("T", bound=object)

stores: Dict[object, object] = dict()


def Injectable() -> Callable:
    def inner(cls: T) -> T:
        orig_init = cls.__init__

        def __init__(self: T, *args, **kwargs) -> None:
            stores.update([[cls, self]])
            orig_init(self, *args, **kwargs)

        cls.__init__ = __init__
        return cls

    return inner


def Inject(StoreClass: object, name: str) -> Callable:
    def inner(cls: T) -> T:
        orig_init = cls.__init__

        def __init__(self: T, *args, **kwargs) -> None:
            if not hasattr(self, "__injected__"):
                self.__injected__ = dict()

            store = stores.get(StoreClass)
            if not store:
                raise ValueError(f'Store with type {StoreClass} is not exists')

            self.__injected__.update([[name, store]])

            orig_init(self, *args, **kwargs)

        cls.__init__ = __init__

        return cls

    return inner
