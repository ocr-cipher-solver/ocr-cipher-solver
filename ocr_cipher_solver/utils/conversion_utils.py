from typing import Any
from typing import Dict
from typing import List

from ocr_cipher_solver.data_formats import PositionalCharacter
from ocr_cipher_solver.data_formats import PositionalCharacterSet


def convert_to_pos_char_set(chars: Dict[str, List[Any]]) -> PositionalCharacterSet:
    """Converts pytesseract character set format to PositionalCharacterSet.

    Parameters
    ----------
    char_set : Dict[str, List[Any]]
        pytesseract character set

    Returns
    -------
    PositionalCharacterSet
        converted positional character set
    """
    return [
        PositionalCharacter.from_tesseract_char(*tess_char)
        for tess_char in zip(
            chars['char'], chars['left'], chars['bottom'], chars['right'], chars['top'],
        )
    ]
