from entities.bullet import Bullet
from entities.enemy import Enemy
from entities.hero import Hero
from scenes.levels_machine import LevelsMachine
from utils.loaders import sound_loader


def load_music() -> None:
    Hero.KILL_SOUND = sound_loader.load("game_over.wav")
    Hero.DESTROY_SOUND = sound_loader.load("enemy_destroy.wav")
    Bullet.SHOOT = sound_loader.load("shoot.mp3")
    Enemy.DESTROY = sound_loader.load("enemy_destroy.wav")
    LevelsMachine.START = sound_loader.load("open_game.wav")
