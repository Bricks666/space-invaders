from typing import Dict

import pygame
from scenes.level1 import Level1

from scenes.scene import Scene


class SceneMachine:
    def __init__(self, screen: pygame.Surface, default: str = "level1"):
        self.scenes: Dict[str, Scene] = {
            "level1": Level1(screen)
        }
        self._current_scene: Scene | None = self.scenes.get(default)

    def select(self, scene: str):
        self._current_scene = self.scenes.get(scene)
    def draw(self):
      if self._current_scene:
        self._current_scene.draw()
    def update(self):
      if self._current_scene:
        self._current_scene.update()
