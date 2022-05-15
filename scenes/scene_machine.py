from typing import Dict

import pygame
from scenes.level import Level
from scenes.scene import Scene


class SceneMachine:
    START: pygame.mixer.Sound

    def __init__(self, screen: pygame.Surface, default: str = "level1"):
        self.scenes: Dict[str, Scene] = {
            "level1": Level(screen, 1),
            "level2": Level(screen, 2)
        }
        self._current_scene_: Scene | None = self.scenes.get(default)
        self._current_scene_.select()
        SceneMachine.START.play()

    def select(self, scene: str):
        if self._current_scene_:
            self._current_scene_.unselect()
        self._current_scene_ = self.scenes.get(scene)
        self._current_scene_.select()

    def draw(self):
        if self._current_scene_:
            self._current_scene_.draw()

    def update(self):
        if self._current_scene_:
            self._current_scene_.update()
