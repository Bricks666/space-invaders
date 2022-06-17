from typing import Dict, List, Optional
from database import DB
from models import LevelModel
from packages.inject import Inject, Injectable


@Injectable()
@Inject(DB, "__db__")
class LevelStore:
    __levels__: List[LevelModel]
    __current_level__: Optional[LevelModel]
    __injected__: Dict[str, object]
    __db__: DB
    __levels_count__: int

    def __init__(self) -> None:
        self.__levels__ = []
        self.__current_level__ = None
        self.__db__ = self.__injected__.get("__db__")

    def get_levels(self) -> List[LevelModel]:
        return self.__levels__

    def change_level(self,  level_id: int) -> Optional[LevelModel]:
        level = self.__get_level_info__(level_id)
        if not level:
            return
        self.__current_level__ = level
        return level

    def get_current_level(self) -> Optional[LevelModel]:
        return self.__current_level__

    def fetch_levels(self) -> None:
        self.__levels__ = self.__db__.levels_table.get_levels()
        self.__levels_count__ = len(self.__levels__)

    def get_levels_count(self) -> None:
        return self.__levels_count__

    def __get_level_info__(self, level_id: int) -> Optional[LevelModel]:
        for level in self.__levels__:
            if level.level_id == level_id:
                return level

        return None
