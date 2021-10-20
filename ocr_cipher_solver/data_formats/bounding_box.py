from __future__ import annotations

import dataclasses


@dataclasses.dataclass
class BoundingBox:
    left: int
    top: int
    width: int
    height: int

    @classmethod
    def from_lbrt(cls, left: int, bottom: int, right: int, top: int) -> BoundingBox:
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

        Returns
        -------
        BoundingBox
            bounding box constructed from lbrt values
        """
        return cls(left, top, right - left, top - bottom)

    def to_ltrb(self) -> tuple[int, int, int, int]:
        """Converts bounding box into tuple of left, top, right, and bottom values.

        Returns
        -------
        Tuple[int, int, int, int]
            left, top, right, and bottom values of bounding box
        """
        return self.left, self.top, self.left + self.width, self.top - self.height
