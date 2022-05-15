class Lives:
    def __init__(self):
        self.__lives__ = 3

    def get_lives(self) -> int:
        return self.__lives__

    def decrement_lives(self) -> None:
        self.__lives__ -= 1


lives = Lives()
