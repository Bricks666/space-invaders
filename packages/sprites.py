import pygame

sprites = pygame.sprite.Group()


class Sprite(pygame.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        sprites.add(self)
        print(self)


def get_all_sprites() -> pygame.sprite.Group:
    return sprites


def get_all_sprites_by_class(cls: object) -> pygame.sprite.Group:
    cls_sprites = pygame.sprite.Group()
    for sprite in sprites:
        if isinstance(sprite, cls):
            cls_sprites.add(sprite)

    return cls_sprites
