import dataclasses


@dataclasses.dataclass
class Position:
    """Stores x and y position (pixel values)."""
    x: int
    y: int
