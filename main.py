from typing import List
import pygame
from consts.main import FPS, HEIGHT, RUNNING, SPRITE_SIZE, WIDTH, Entities
from enemies.enemy import Enemy

from enemies.hero import Hero


def controll_events():
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                global RUNNING
                RUNNING = False


all_sprites = pygame.sprite.Group()


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space invader")
    clock = pygame.time.Clock()
    global RUNNING
    RUNNING = True
    fill_sprites_by_level(1)
    while RUNNING:
        screen.fill((0, 0, 0))
        all_sprites.update()
        all_sprites.draw(screen)
        controll_events()
        pygame.display.update()
        clock.tick(FPS)


def fill_sprites_by_level(level: int):
    with open(f"./levels/level{level}.txt", "r") as level:
        sprites: List[str] = [line.strip() for line in level]
        print(sprites)
        for y in range(len(sprites)):
            enemies = 0
            total_enemies_count = sprites[y].count(Entities.ENEMY.value)
            for x in range(len(sprites[y])):
                position = (x * SPRITE_SIZE, y * SPRITE_SIZE)
                match sprites[y][x]:
                    case Entities.ENEMY.value:
                        print("enemy", position)
                        all_sprites.add(Enemy(*position, enemies, total_enemies_count))
                        enemies += 1
                    case Entities.HERO.value:
                        print("hero", position)
                        all_sprites.add(Hero(*position))


if __name__ == "__main__":
    main()
