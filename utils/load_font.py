from typing import Dict
from components.text import Text, _FontSizes
from utils.loaders import font_loader

size_to_pixels: Dict[_FontSizes, int] = {
    "small": 14,
    "normal": 18,
    "large": 24
}


def load_font() -> None:
    for size, pixels in size_to_pixels.items():
        Text.fonts.update(
            [[size, font_loader.load("PublicPixel.ttf", pixels)]])
