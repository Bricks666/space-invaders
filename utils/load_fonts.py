from typing import Dict
from components.text import Text, _FontSizes
from utils.loaders import font_loader

size_to_pixels: Dict[_FontSizes, int] = {
    "small": 14,
    "normal": 18,
    "large": 24
}
"""
Карта размеров шрифта к литеральным значениям
"""


def load_fonts() -> None:
    """
    Функция для загрузки и сохранения шрифтов
    """
    for size, pixels in size_to_pixels.items():
        Text.fonts.update(
            [[size, font_loader.load("PublicPixel.ttf", pixels)]])
