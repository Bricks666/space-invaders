from entities.text import Text
from utils.loaders import font_loader


def load_font() -> None:
    Text.FONT = font_loader.load("PublicPixel.ttf")
