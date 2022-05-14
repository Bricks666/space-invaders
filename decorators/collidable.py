from msilib.schema import Class
import pygame


collidable_sprites = pygame.sprite.Group()

def add_collidable(cls: pygame.sprite.Sprite):
  orig_init = cls.__init__
