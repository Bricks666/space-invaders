from typing import Literal, NamedTuple
from ..math import VectorLike, Sizes


VerticalAnchor = Literal['top', 'center', 'bottom']
HorizontalAnchor = Literal['left', 'center', 'right']


class Anchors(NamedTuple):
    vertical: VerticalAnchor = 'center'
    horizontal: HorizontalAnchor = 'center'


class SpritePositionOptions(NamedTuple):
    scale: VectorLike = VectorLike(1)
    offset: VectorLike = VectorLike()
    """
    Relative offset from (0, 0) of game object
    """
    sizes: Sizes = Sizes()
