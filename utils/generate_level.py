from typing import List, Tuple
import pygame
from consts.main import SPRITE_SIZE,  Entities
from enemies.hero import Hero
from enemies.enemy import Enemy


def generate_level(level: int) -> Tuple[pygame.sprite.Group, pygame.sprite.Group]:
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    with open(f"./levels/level{level}.txt", "r") as level:
        sprites: List[str] = [line.strip() for line in level]
        print(sprites)
        for y in range(len(sprites)):
            enemies_count = 0
            total_enemies_count = sprites[y].count(Entities.ENEMY.value)
            for x in range(len(sprites[y])):
                position = (x * SPRITE_SIZE, y * SPRITE_SIZE)
                match sprites[y][x]:
                    case Entities.ENEMY.value:
                        enemy = Enemy(*position, enemies_count,
                                      total_enemies_count)
                        all_sprites.add(enemy)
                        enemies_count += 1
                        enemies.add(enemy)
                    case Entities.HERO.value:
                        all_sprites.add(Hero(*position))

    return all_sprites, enemies
