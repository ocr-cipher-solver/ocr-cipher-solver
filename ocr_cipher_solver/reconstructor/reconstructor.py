from PIL import Image

from ocr_cipher_solver.data_formats import PositionalCharacterSet


ReconstructedImage = Image.Image


class Reconstructor:
    """Handles reconstructing of image from input and ciphered character set."""

    def run(
        self, ciphered_char_set: PositionalCharacterSet, input_image: Image.Image,
    ) -> ReconstructedImage:
        """Runs reconstruction on image.

        Parameters
        ----------
        ciphered_char_set : PositionalCharacterSet
            enciphered character set to overlay on image
        input_image : Image.Image
            image to use as base for reconstructed image

        Returns
        -------
        ReconstructedImage
            image created from overlaying ciphered characters on input image
        """
        ...
