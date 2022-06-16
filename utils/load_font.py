from entities.text import Text
from utils.loaders import font_loader


def load_font() -> None:
    Text.font = font_loader.load("PublicPixel.ttf")
