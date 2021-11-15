from typing import List

import pytest

from ocr_cipher_solver.ciphers import CaesarianCipher
from ocr_cipher_solver.data_formats.bounding_box import BoundingBox
from ocr_cipher_solver.data_formats.character import Character
from ocr_cipher_solver.data_formats.positional_character import PositionalCharacter
from ocr_cipher_solver.data_formats.positional_character import PositionalCharacterSet


def charset_to_chars(charset: PositionalCharacterSet) -> List[Character]:
    return [char.character for char in charset]


def chars_to_charset(chars: List[Character]) -> PositionalCharacterSet:
    return [PositionalCharacter(char, BoundingBox(0, 0, 0, 0)) for char in chars]


@pytest.mark.parametrize(
    ('input_char', 'expected_output_char', 'shift'),
    (('a', 'b', 1), ('b', 'a', -1), ('f', 'k', 5)),
)
def test_caesarian_cipher_enciphers_single_character_correctly(
    input_char, expected_output_char, shift,
):
    """Tests that caesarian cipher computes correct output character given an input and a shift."""
    # create caesarian cipher object (arrange step)
    cipher = CaesarianCipher(shift)

    # run cipher on the input character (act step)
    (output_char,) = charset_to_chars(cipher.run(chars_to_charset((input_char,))))

    # check that output character is as expected
    assert expected_output_char == output_char


@pytest.mark.parametrize(
    ('input_chars', 'expected_output_chars', 'shift'),
    ((('a', 'b'), ('b', 'c'), 1), (('b', 'a'), ('a', 'z'), -1), (('f', 'a'), ('k', 'f'), 5)),
)
def test_caesarian_cipher_enciphers_multiple_characters_correctly(
    input_chars, expected_output_chars, shift,
):
    """Tests that caesarian cipher computes correct output characters given inputs and a shift."""
    # create caesarian cipher object (arrange step)
    cipher = CaesarianCipher(shift)

    # run cipher on the input character (act step)
    output_chars = charset_to_chars(cipher.run(chars_to_charset(input_chars)))

    # check that output character is as expected
    assert list(expected_output_chars) == output_chars
