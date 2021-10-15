"""Defines the OCR class, which transforms an image of text to characters and bounding boxes."""
import easyocr
import numpy as np
import utils
from PIL import Image

from .data_formats import PositionalCharacterSet


class OCR:
    def __init__(self):
        """OCR class, used to generate positional character set from image."""
        # create an english OCR reader
        self._reader = easyocr.Reader(['en'])

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
        # perform OCR on input image
        recognized_characters = self._reader.readtext(np.asarray(input_image))

        return utils.convert_to_pos_char_set(recognized_characters)
