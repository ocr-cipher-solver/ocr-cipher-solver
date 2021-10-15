from __future__ import annotations

import dataclasses
from typing import List

from .bounding_box import BoundingBox
from .character import Character
from .position import Position


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
    def from_easy_ocr_char(
        cls, ocr_char: tuple[list[list[int]], str, float],
    ) -> PositionalCharacter:
        """Creates positional character from easy OCR character.

        Parameters
        ----------
        char : Tuple[List[List[int]], str, float]
            tuple of bounding box, character, and confidence

        Returns
        -------
        PositionalCharacter
            positional character constructed form easy ocr character
        """
        # unpack easy ocr char
        bounding_box, char, _ = ocr_char
        return cls(
            character=char,
            bounding_box=BoundingBox(*tuple(Position(*corner) for corner in bounding_box)),
        )


PositionalCharacterSet = List[PositionalCharacter]
