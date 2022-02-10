"""Identity cipher."""
from .base import Encipherer
from ocr_cipher_solver.data_formats import PositionalCharacterSet


class IdentityEncipherer(Encipherer):
    """Performs identity enciphering (no change to characters)."""

    def run(self, input_char_set: PositionalCharacterSet) -> PositionalCharacterSet:
        """Returns identity of input character set (identical character set).

        Parameters
        ----------
        input_char_set : PositionalCharacterSet
            character set to encipher

        Returns
        -------
        PositionalCharacterSet
            same character set as was inputted
        """
        return input_char_set
