class Vector:
  x: float
  y: float

  def __init__(self, x: float = 0, y: float = 0) -> None:
    super().__init__()
    self.x = x
    self.y = y
