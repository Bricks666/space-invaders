from database import DB
from packages.inject import Injector


@Injector.injectable()
@Injector.inject(DB, "__db__")
class LivesStore:
    __lives__: int
    __db__: DB

    def __init__(self) -> None:
        self.__lives__ = 0


    def fetch_lives(self, level_id: int) -> None:
        self.__lives__ = self.__db__.levels_table.get_lives_on_level(
            level_id) or 0

    def get_lives(self) -> int:
        return self.__lives__

    def decrement_lives(self) -> None:
        self.__lives__ -= 1

    def reset(self) -> None:
        self.__lives__ = 0
