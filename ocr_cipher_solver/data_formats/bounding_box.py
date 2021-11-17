from __future__ import annotations

import dataclasses
import enum


class Coords(enum.Enum):
    """Coordinate types."""
    BottomLeft = enum.auto()
    TopLeft = enum.auto()


@dataclasses.dataclass
class BoundingBox:
    left: int
    top: int
    width: int
    height: int
    img_width: int
    img_height: int

    @classmethod
    def from_lbrt(cls, left: int, bottom: int, right: int, top: int, img_width: int, img_height: int) -> BoundingBox:
        """Generates bounding box from left, bottom, right, and top values.

        Parameters
        ----------
        left : int
            distance from left of bounding box to left edge of image
        bottom : int
            distance from bottom of bounding box to bottom edge of image
        right : int
            distance from right of bounding box to right edge of image
        top : int
            distance from top of bounding box to top edge of image
        img_width : int
            width of image
        img_height : int
            height of image

        Returns
        -------
        BoundingBox
            bounding box constructed from lbrt values
        """
        return cls(left, top, right - left, top - bottom, img_width, img_height)

    def to_ltrb(self, coords: Coords = Coords.BottomLeft) -> tuple[int, int, int, int]:
        """Converts bounding box into tuple of left, top, right, and bottom values.

        Parameters
        ----------
        coords : Coords
            coordinate scheme to use, by default BottomLeft origin coordinates

        Returns
        -------
        Tuple[int, int, int, int]
            left, top, right, and bottom values of bounding box
        """
        if coords == Coords.BottomLeft:
            return self.left, self.top, self.left + self.width, self.top - self.height
        elif coords == Coords.TopLeft:
            return self.left, self.img_height - self.top, self.left + self.width, self.img_height - (self.top - self.height)
        else:
            raise ValueError(f'Invalid value {coords} for coordinate scheme.')
