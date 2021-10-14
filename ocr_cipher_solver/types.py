from typing import List
from typing import Tuple

Character = str


Position = Tuple[int, int]


BoundingBox = Tuple[Position, Position, Position, Position]


PositionalCharacter = Tuple[Character, BoundingBox]


PositionalCharacterSet = List[PositionalCharacter]
