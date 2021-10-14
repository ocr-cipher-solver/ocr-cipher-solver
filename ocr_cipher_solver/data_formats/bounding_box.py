import dataclasses

from .position import Position


@dataclasses.dataclass
class BoundingBox:
    top_left: Position
    top_right: Position
    bottom_left: Position
    bottom_right: Position
