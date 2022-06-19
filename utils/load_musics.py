from components.button import Button
from entities.enemy import Enemy
from entities.hero import Hero, HeroBullet
from screens.level import Level
from screens.levels import Levels
from screens.menu import Menu
from utils.loaders import sound_loader


def load_musics() -> None:
    """
    Функция для загрузки нужных звуков и сохранения их в сущностях
    """
    HeroBullet.set_music("shoot", sound_loader.load("shoot.wav"))
    Enemy.set_music("destroy", sound_loader.load("invaderkilled.wav"))
    Enemy.set_music("step", sound_loader.load("fastinvader1.wav"))
    Hero.set_music("explosion", sound_loader.load("explosion.wav"))
    Button.set_sound("click", sound_loader.load("button_click.wav"))
    Menu.set_music("game_start", sound_loader.load("menu.mpeg"))
    Levels.set_music("game_start", sound_loader.load("menu.mpeg"))
    Level.set_music("level_start", sound_loader.load("level.wav"))
