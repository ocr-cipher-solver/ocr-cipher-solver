"""Defines the OCR class, which transforms an image of text to characters and bounding boxes."""
from PIL import Image

from .types import PositionalCharacterSet


class OCR:
    def __init__(self):
        """OCR class, used to generate positional character set from image."""
        ...

    def run(self, input_image: Image.Image) -> PositionalCharacterSet:
        """Runs OCR on image, returns positional character set.

        Parameters
        ----------
        input_image : Image.Image
            image to run OCR on

        Returns
        -------
        PositionalCharacterSet
            character set read from image, with positions
        """
        ...
