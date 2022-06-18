from packages.core import Screen
from screens.level.aside import Aside
from screens.level.level_place import LevelPlace


class Level(Screen):
    def activate(self, *args) -> None:
        self.__musics__.get("start").play()
        self.__parts__.append(LevelPlace(self.__screen__))
        self.__parts__.append(Aside(self.__screen__))
        return super().activate(*args)
