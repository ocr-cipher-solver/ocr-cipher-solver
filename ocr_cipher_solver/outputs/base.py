import abc

from PIL import Image

from ocr_cipher_solver.data_formats.positional_character import PositionalCharacterSet


class PipelineOutput(abc.ABC):
    """Pipeline output base class."""
    @abc.abstractmethod
    def run(self, output_image: Image.Image, enciphered_positional_character_set: PositionalCharacterSet):
        """Runs output operation on output image.

        Parameters
        ----------
        output_image : Image.Image
            image to run output operation on
        enciphered_char_set : PositionalCharacterSet
            enciphered character set to run output operation on
        """
        raise NotImplementedError
