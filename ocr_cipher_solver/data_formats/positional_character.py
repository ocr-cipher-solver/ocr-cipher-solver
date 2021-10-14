import dataclasses
from typing import List

from .bounding_box import BoundingBox
from .character import Character


@dataclasses.dataclass
class PositionalCharacter:
    character: Character
    bounding_box: BoundingBox

    def __post_init__(self):
        """Checks that character string is of length one."""
        if len(self.character) != 1:
            raise ValueError(
                f'Character cannot be longer than length one, has length {len(self.character)}.',
            )


PositionalCharacterSet = List[PositionalCharacter]
