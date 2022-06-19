from typing import List, Optional
from database import DB
from models import LevelModel
from packages.inject import Injector


@Injector.injectable()
@Injector.inject(DB, "__db__")
class LevelStore:
    """
    Хранилище данных об уровнях и текущем уровне
    """
    __levels__: List[LevelModel]
    """
    Список всех уровней
    """
    __current_level__: Optional[LevelModel]
    """
    Текущий уровень
    """
    __db__: DB
    """
    БД
    """

    def __init__(self) -> None:
        self.__levels__ = []
        self.__current_level__ = None

    def get_levels(self) -> List[LevelModel]:
        """
        Метод для получения всех уровней
        """
        return self.__levels__

    def change_level(self,  level_id: int) -> Optional[LevelModel]:
        """
        Метод для изменения уровня
        """
        level = self.__get_level_info__(level_id)
        if not level:
            """
            Чтобы не сломать текущий уровень,
            ничего не меняем, если такого уровня нет
            """
            return
        self.__current_level__ = level
        return level

    def get_current_level(self) -> Optional[LevelModel]:
        """
        Метод для получения текущего уровня
        """
        return self.__current_level__

    def fetch_levels(self) -> None:
        """
        Загрузка уровней из БД
        """
        self.__levels__ = self.__db__.levels_table.get_levels()

    def __get_level_info__(self, level_id: int) -> Optional[LevelModel]:
        """
        Получение информации об уровне
        """
        for level in self.__levels__:
            """
            Так как Id уровня может не совпадать с их индексом
            """
            if level.level_id == level_id:
                return level

        return None
