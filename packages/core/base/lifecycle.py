from abc import ABC


class BaseLifecycleMethods(ABC):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__()

    def init(self, *args, **kwargs) -> None:
        pass

    def activate(self, *args, **kwargs) -> None:
        pass

    def update(self, *args, **kwargs) -> None:
        pass

    def deactivate(self, *args, **kwargs) -> None:
        pass

    def kill(self, *args, **kwargs) -> None:
        pass


class DrawableLifecycleMethods(BaseLifecycleMethods):
    def draw(self, *args, **kwargs) -> None:
        pass
