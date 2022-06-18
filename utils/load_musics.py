from entities.bullet import Bullet
from entities.enemy import Enemy
from entities.hero import Hero
from screens.level import Level
from utils.loaders import sound_loader


def load_musics() -> None:
    Bullet.SHOOT = sound_loader.load("shoot.mp3")
    Enemy.set_music("destroy", sound_loader.load("enemy_destroy.wav"))
    Hero.set_music("kill", sound_loader.load("game_over.wav"))
    Hero.set_music("destroy", sound_loader.load("enemy_destroy.wav"))
    Level.__musics__.update([["start", sound_loader.load("open_game.wav")]])
