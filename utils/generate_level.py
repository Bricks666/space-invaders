from typing import List, Tuple
import pygame
from consts.main import SCREEN_MARGIN, SPRITE_SIZE,  Entities
from entities.hero import Hero
from entities.enemy import Enemy
from utils.loaders import level_loader


def generate_level(level: int) -> Tuple[pygame.sprite.Group, pygame.sprite.Group]:
    sprites = level_loader.load(f'level{level}.txt')
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    players = pygame.sprite.Group()
    for y in range(len(sprites)):
        enemies_count = 0
        total_enemies_count = sprites[y].count(Entities.ENEMY.value)
        for x in range(len(sprites[y])):
            position = (x * SPRITE_SIZE + SCREEN_MARGIN,
                        y * SPRITE_SIZE + SCREEN_MARGIN)
            match sprites[y][x]:
                case Entities.ENEMY.value:
                    enemy = Enemy(*position, enemies_count,
                                  total_enemies_count)
                    all_sprites.add(enemy)
                    enemies_count += 1
                    enemies.add(enemy)
                case Entities.HERO.value:
                    hero = Hero(*position)
                    all_sprites.add(hero)
                    players.add(hero)

    return all_sprites, enemies, players
