from typing import List
from typing import Tuple

from ocr_cipher_solver.data_formats import PositionalCharacter
from ocr_cipher_solver.data_formats import PositionalCharacterSet


def convert_to_pos_char_set(
    char_set: List[Tuple[List[List[int]], str, float]],
) -> PositionalCharacterSet:
    """Converts EasyOCR character set format to PositionalCharacterSet.

    Parameters
    ----------
    char_set : List[Tuple[List[List[int]], str, float]]
        easyocr character set
        list of tuples of bounding boxes, characters, and confidence values

    Returns
    -------
    PositionalCharacterSet
        converted positional character set
    """
    return [
        PositionalCharacter.from_easy_ocr_char(char) for char in char_set
    ]
