from consts import SCREEN_MARGIN, SPRITE_SIZE,  Entities
from entities.hero import Hero
from entities.enemy import Enemy
from utils.loaders import level_loader


def generate_level(level_path: str) -> None:
    sprites = level_loader.load(level_path)
    for y in range(len(sprites)):
        enemies_count = 0
        total_enemies_count = sprites[y].count(Entities.ENEMY.value)
        for x in range(len(sprites[y])):
            position = (x * SPRITE_SIZE + SCREEN_MARGIN,
                        y * SPRITE_SIZE + SCREEN_MARGIN)
            match sprites[y][x]:
                case Entities.ENEMY.value:
                    Enemy(*position, enemies_count,
                          total_enemies_count)
                    enemies_count += 1
                case Entities.HERO.value:
                    Hero(*position)
