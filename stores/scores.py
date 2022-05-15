class Scores:
    def __init__(self):
        self.__max_scores__ = 0
        self.__value__ = 0

    def init(self, max_scores: int):
        self.__max_scores__ = max_scores

    def add(self, value: int) -> None:
        self.__value__ += value

    def get_scores(self) -> int:
        return self.__value__

    def get_max_scores(self) -> int:
        return self.__max_scores__

    def reset_score(self) -> None:
        self.__max_scores__ = max(self.__max_scores__, self.__value__)
        self.__value__ = 0


scores = Scores()
