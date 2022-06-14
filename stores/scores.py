from packages.inject import Injectable


@Injectable()
class ScoresStore:
    def __init__(self, max_score: int = 0):
        self.__max_scores__ = max_score
        self.__value__ = 0

    def add(self, value: int) -> None:
        self.__value__ += value

    def get_scores(self) -> int:
        return self.__value__

    def get_max_scores(self) -> int:
        return self.__max_scores__

    def reset_score(self) -> None:
        self.__max_scores__ = max(self.__max_scores__, self.__value__)
        self.__value__ = 0
