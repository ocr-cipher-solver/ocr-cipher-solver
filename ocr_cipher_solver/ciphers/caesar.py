from ocr_cipher_solver.ciphers.base import Encipherer
from ocr_cipher_solver.data_formats import PositionalCharacter
from ocr_cipher_solver.data_formats import PositionalCharacterSet


class CaesarianCipher(Encipherer):
    """Caesarian cipher implementation."""

    def __init__(self, shift: int):
        """Creates caesar cipher with given shift.

        Parameters
        ----------
        shift : int
            shift to apply to characters (in positive direction)
        """
        self._shift = shift

    def run(self, pos_char_set: PositionalCharacterSet) -> PositionalCharacterSet:
        """Runs caesar cipher on provided positional character set and returns ciphered set.

        Parameters
        ----------
        pos_char_set : PositionalCharacterSet
            input positional character set

        Returns
        -------
        PositionalCharacterSet
            ciphered positional character set
        """
        return [
            PositionalCharacter(self._rotate(input_char.character), input_char.bounding_box)
            for input_char in pos_char_set
        ]

    def _rotate(self, char: str) -> str:
        """Rotates character by <self._shift>.

        Parameters
        ----------
        char : str
            character to rotate

        Returns
        -------
        str
            rotated character
        """
        # compute character offset
        num_chars = 26
        if char.isupper():
            offset = 65
        else:
            offset = 97

        # shift character
        return chr(((ord(char) + self._shift - offset) % num_chars) + offset)
