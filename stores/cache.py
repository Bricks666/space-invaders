from typing import Any, Dict, TypeVar, Union
from packages.inject import Injector


T = TypeVar("T", bound=Any)


@Injector.injectable()
class Cache:
    __cached__: Dict[str, Any]

    def __init__(self) -> None:
        self.__cached__ = {}

    def get(self, key: str) -> Union[T, None]:
        return self.__cached__.get(key)

    def set(self, key: str, value: T) -> None:
        self.__cached__.update([[key, value]])
