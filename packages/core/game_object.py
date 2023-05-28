from .aabb import AABB
from pygame import Surface
from .scripts import Scriptable
from .views import Viewable
from .collidable import Collidable


class GameObject(Collidable, Scriptable, Viewable):
    __killed: bool

    def __init__(self, *args, **kwargs) -> None:
        print(self.__class__.__name__)
        Collidable.__init__(self, *args, **kwargs)
        Scriptable.__init__(self, *args, **kwargs)
        Viewable.__init__(self, *args, **kwargs)
        self.__killed = False

    def update(self, *args, **kwargs):
        Scriptable.update(self)
        Collidable.update(self, *args, **kwargs)

    def kill(self) -> None:
        if self.__killed:
            return
        self.__killed = True
        Scriptable.kill(self)
        Collidable.kill(self)
