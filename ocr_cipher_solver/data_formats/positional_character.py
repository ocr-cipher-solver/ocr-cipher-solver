from __future__ import annotations

import dataclasses
from typing import List
from typing import Tuple

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

    @classmethod
    def from_tesseract_char(
        cls, char: Character, left: int, bottom: int, right: int, top: int, image_shape: tuple[int, int],
    ) -> PositionalCharacter:
        """Creates positional character from tesseract character.

        Parameters
        ----------
        char : Character
            tesseract detected character
        left : int
            distance from left of bounding box to left edge of image
        bottom : int
            distance from bottom of bounding box to bottom edge of image
        right : int
            distance from right of bounding box to right edge of image
        top : int
            distance from top of bounding box to top edge of image
        image_shape : Tuple[int, int]
            shape of image

        Returns
        -------
        PositionalCharacter
            positional character constructed from tesseract character
        """
        return cls(
            character=char,
            bounding_box=BoundingBox.from_lbrt(left, bottom, right, top, *image_shape),
        )


PositionalCharacterSet = List[PositionalCharacter]
