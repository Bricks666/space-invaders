from typing import Dict

import pygame
from scenes.level1 import Level1
from scenes.scene import Scene


class SceneMachine:
    def __init__(self, screen: pygame.Surface, default: str = "level1"):
        self.scenes: Dict[str, Scene] = {
            "level1": Level1(screen)
        }
        self._current_scene_: Scene | None = self.scenes.get(default)
        self._current_scene_.select()

    def select(self, scene: str):
        if self._current_scene_:
            self._current_scene_.unselect()
        self._current_scene_ = self.scenes.get(scene)
        self._current_scene_.select

    def draw(self):
        if self._current_scene_:
            self._current_scene_.draw()

    def update(self):
        if self._current_scene_:
            self._current_scene_.update()
