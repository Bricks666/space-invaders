from typing import Set, Callable, Any, Dict, Self


_Callback = Callable[[], Any]
_Listeners = Set[_Callback]
_Subscribers = Dict[str, _Listeners]


class EventEmitter:
    __subscribers: _Subscribers

    def __init__(self) -> None:
        self.__subscribers = {}

    def subscribe(self, event: str, callback: _Callback) -> Self:
        if event not in self.__subscribers:
            self.__subscribers[event] = set()
        self.__subscribers[event].add(callback)
        return self

    def unsubscribe(self, event: str, callback: _Callback) -> Self:
        self.__subscribers[event].remove(callback)
        if len(self.__subscribers[event]) == 0:
            del self.__subscribers[event]
        return self

    def unsubscribe_all(self, event: str) -> Self:
        self.__subscribers[event].clear()
        del self.__subscribers[event]
        return self

    def subscribers(self, event: str) -> _Listeners | None:
        return self.__subscribers.get(event)
