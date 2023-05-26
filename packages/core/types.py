from abc import ABC


class LifecycleMethods(ABC):

    def init(self, *args, **kwargs):
        pass

    def activate(self, *args, **kwargs):
        pass

    def update(self, *args, **kwargs):
        pass

    def deactivate(self, *args, **kwargs):
        pass

    def kill(self, *args, **kwargs):
        pass
