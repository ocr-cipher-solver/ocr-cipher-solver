from PIL import Image
from ocr_cipher_solver import outputs

from ocr_cipher_solver.data_formats.positional_character import PositionalCharacterSet
from ocr_cipher_solver.outputs.base import PipelineOutput


class ShowImage(PipelineOutput):
    """Shows image."""
    def run(self, output_image: Image.Image, enciphered_positional_character_set: PositionalCharacterSet):
        """Shows output image.

        Parameters
        ----------
        output_image : Image.Image
            image to run output operation on
        enciphered_char_set : PositionalCharacterSet
            enciphered character set to run output operation on
        """
        # show output image
        output_image.show()
