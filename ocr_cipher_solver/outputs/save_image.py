import pathlib

from PIL import Image

from ocr_cipher_solver.data_formats.positional_character import PositionalCharacterSet
from ocr_cipher_solver.outputs.base import PipelineOutput


class SaveImage(PipelineOutput):
    """Saves image."""
    def __init__(self, save_path: pathlib.Path):
        self._save_path = save_path

    def run(self, output_image: Image.Image, enciphered_positional_character_set: PositionalCharacterSet):
        """Saves output image.

        Parameters
        ----------
        output_image : Image.Image
            image to run output operation on
        enciphered_char_set : PositionalCharacterSet
            enciphered character set to run output operation on
        """
        # save output image
        output_image.save(self._save_path)
