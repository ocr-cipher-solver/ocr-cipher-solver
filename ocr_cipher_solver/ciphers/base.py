import abc

from ocr_cipher_solver.data_formats import PositionalCharacterSet


class Encipherer(abc.ABC):
    @abc.abstractmethod
    def run(self, input_char_set: PositionalCharacterSet) -> PositionalCharacterSet:
        """Runs cipher algorithm on character set, returns ciphered character set.

        Parameters
        ----------
        input_char_set : PositionalCharacterSet
            character set to encipher

        Returns
        -------
        PositionalCharacterSet
            ciphered character set, constructed from input charcter set
        """
        raise NotImplementedError
