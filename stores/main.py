from typing import Any, TypeVar

T = TypeVar("T", bound=object)


def inject(store: Any, name: str):
    def inner(cls: T) -> T:
        orig_init = cls.__init__

        def __init__(self: object, *args, **kwargs):
            if not hasattr(self, "__injected__"):
                self.__injected__ = dict()
            self.__injected__.update([[name, store]])
            orig_init(self, *args, **kwargs)
        cls.__init__ = __init__
        return cls

    return inner
