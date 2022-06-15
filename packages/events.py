from enum import Enum

import pygame


class CustomEventsTypes(Enum):
    RESTART = pygame.USEREVENT + 1


def emit_event(evt: pygame.event.Event) -> None:
    pygame.event.post(evt)
