from typing import List


def load_level(level: int) -> List[str]:

    with open(f"./levels/level{level}.txt", "r") as level:
        return [line.strip() for line in level]
