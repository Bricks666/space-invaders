import pygame
from consts.main import FPS, HEIGHT, RUNNING, WIDTH
from scenes.scene_machine import SceneMachine
from utils.load_music import load_music


def main():

    def controll_events():
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    global RUNNING
                    RUNNING = False
                case pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_1]:
                        scene_machine.select("level1")
                    if keys[pygame.K_2]:
                        scene_machine.select("level2")

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space invader")
    pygame.mixer.init()
    load_music()
    scene_machine = SceneMachine(screen)

    clock = pygame.time.Clock()
    global RUNNING
    RUNNING = True
    while RUNNING:
        screen.fill((0, 0, 0))
        scene_machine.update()
        scene_machine.draw()
        controll_events()
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
