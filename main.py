import pygame
from consts.main import FPS, HEIGHT, RUNNING, WIDTH
from scenes.scene_machine import SceneMachine


def controll_events():
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                global RUNNING
                RUNNING = False




def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space invader")
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
