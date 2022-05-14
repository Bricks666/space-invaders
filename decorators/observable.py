import pygame


def observable(collection: pygame.sprite.Group):
  def inner(c):
    print(c)
    return c
  return inner
