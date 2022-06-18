from typing import Callable, Dict, List, TypeVar, final


T = TypeVar("T", bound=object)


@final
class Injector:
    __injectable_dict__: Dict[str, object] = {}
    __injectable_list__: List[object] = []

    @classmethod
    def inject(cls, store_class: object, name: str) -> Callable:
        def inner(injectable: T) -> T:
            orig_init = injectable.__init__

            def __init__(self: T, *args, **kwargs) -> None:
                if not hasattr(self, "__injected__"):
                    self.__injected__ = dict()

                store = cls.__injectable_dict__.get(store_class)
                if not store:
                    raise ValueError(
                        f'Store with type {store_class} is not exists')

                self.__injected__.update([[name, store]])

                orig_init(self, *args, **kwargs)

            injectable.__init__ = __init__

            return injectable

        return inner

    @classmethod
    def injectable(cls) -> Callable:
        def inner(injectable: T) -> T:
            cls.__injectable_list__.append(injectable)
            return injectable

        return inner

    @classmethod
    def init(cls) -> None:
        for injectable in cls.__injectable_list__:
            cls.__injectable_dict__.update([[injectable, injectable()]])
