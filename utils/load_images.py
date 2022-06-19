from entities.enemy import Enemy
from entities.hero import Hero
from utils.loaders import sprite_loader


def load_images() -> None:
    """
    Метод для загрузки картинок и сохранения их в сущностях
    """
    Hero.set_image("hero", sprite_loader.load("hero.png"))
    Hero.set_image("hero_bullet",  sprite_loader.load("hero_bullet.png"))
    Enemy.set_image("enemy", sprite_loader.load("enemy.png"))
    Enemy.set_image("enemy_bullet",  sprite_loader.load("enemy_bullet.png"))
