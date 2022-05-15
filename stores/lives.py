class Lives:
    __START__ = 3

    def __init__(self):
        self.__lives__ = self.__START__

    def get_lives(self) -> int:
        return self.__lives__

    def decrement_lives(self) -> None:
        self.__lives__ -= 1

    def reset(self):
        self.__lives__ = self.__START__


lives = Lives()
