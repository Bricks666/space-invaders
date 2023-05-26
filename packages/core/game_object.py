from .aabb import AABB
from .scripts import Scriptable
from .collidable import Collidable


class GameObject(Collidable, Scriptable):

    def __init__(self, *args) -> None:
        print(self.__class__.__name__)
        super().__init__(*args)
        Collidable.__init__(self, *args)
        Scriptable.__init__(self)

    def update(self, *args, **kwargs):
        Scriptable.update(self)
        Collidable.update(self, *args, **kwargs)
