from packages.inject import Injectable


@Injectable()
class LivesStore:

    def __init__(self):
        self.__lives__ = 0
        self.__max_lives__ = 0

    def set_lives(self, lives: int) -> None:
        self.__lives__ = self.__max_lives__ = lives

    def get_lives(self) -> int:
        return self.__lives__

    def decrement_lives(self) -> None:
        self.__lives__ -= 1

    def reset(self) -> None:
        self.__lives__ = self.__max_lives__
