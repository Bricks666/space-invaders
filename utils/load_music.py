from entities.bullet import Bullet
from entities.enemy import Enemy
from entities.hero import Hero
from scenes.scene_machine import SceneMachine
from utils.loaders import sound_loader


def load_music() -> None:
    Hero.KILL_SOUND = sound_loader.load("game_over.wav")
    Bullet.SHOOT = sound_loader.load("shoot.mp3")
    Enemy.DESTROY = sound_loader.load("enemy_destroy.wav")
    SceneMachine.START = sound_loader.load("open_game.wav")
