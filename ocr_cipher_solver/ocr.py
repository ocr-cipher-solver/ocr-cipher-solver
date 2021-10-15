"""Defines the OCR class, which transforms an image of text to characters and bounding boxes."""
import numpy as np
import pytesseract
from PIL import Image

from . import utils
from .data_formats import PositionalCharacterSet


class OCR:
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
        recognized_characters = pytesseract.image_to_boxes(
            np.asarray(input_image), output_type=pytesseract.Output.DICT,
        )

        return utils.convert_to_pos_char_set(recognized_characters)
