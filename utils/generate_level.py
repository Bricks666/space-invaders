from typing import Tuple
from consts import SCREEN_MARGIN, SPRITE_SIZE,  EntityCodes
from entities.hero import Hero
from entities.enemy import Enemy
from packages.core import Group
from utils.loaders import level_loader
from pygame import sprite


def generate_level(level_path: str) -> Tuple[Group[sprite.Sprite], Group[Enemy], Group[Hero]]:
    sprite_codes = level_loader.load(level_path)
    all_sprites = Group[sprite.Group]()
    enemies = Group[Enemy]()
    heros = Group[Hero]()
    for y in range(len(sprite_codes)):
        enemies_count = 0
        total_enemies_count = sprite_codes[y].count(EntityCodes.ENEMY.value)
        for x in range(len(sprite_codes[y])):
            position = (x * SPRITE_SIZE + SCREEN_MARGIN,
                        y * SPRITE_SIZE + SCREEN_MARGIN)
            match sprite_codes[y][x]:
                case EntityCodes.ENEMY.value:
                    enemy = Enemy(*position, enemies_count,
                                  total_enemies_count, [all_sprites])
                    all_sprites.add(enemy)
                    enemies.add(enemy)
                    enemies_count += 1
                case EntityCodes.HERO.value:
                    hero = Hero(*position, [all_sprites])
                    all_sprites.add(hero)
                    heros.add(hero)

    return all_sprites, enemies, heros
