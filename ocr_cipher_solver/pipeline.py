"""Defines the image processing pipeline."""
from typing import Tuple

from PIL import Image

from .ciphers import Encipherer
from .ocr import OCR
from .outputs import PipelineOutput
from .reconstructor import ReconstructedImage
from .reconstructor import Reconstructor
from ocr_cipher_solver.types import PositionalCharacterSet


class ImagePipeline:
    """Defines the image processing pipeline for the OCR cipher solver."""

    def __init__(
        self,
        ocr: OCR,
        encipherer: Encipherer,
        reconstructor: Reconstructor,
        outputs: Tuple[PipelineOutput],
    ):
        """Creates an image pipeline with the provided encipherer, OCR, and Reconstructor.

        Parameters
        ----------
        ocr : OCR
            OCR class to use for pipeline
        encipherer : Encipherer
            encipherer to use for image transformation
        reconstructor : Reconstructor
            image reconstructor to use for pipeline
        outputs : Tuple[PipelineOutput]
            tuple of pipeline output steps, to run at end of pipeline
        """
        # set pipeline stages
        self._ocr = ocr
        self._encipherer = encipherer
        self._reconstructor = reconstructor
        self._outputs = outputs

    def run_pipeline(self, input_image: Image.Image):
        """Runs pipeline, feeding results forward through stages.

        Parameters
        ----------
        input_image : Image.Image
            image to run pipeline with
        """
        # run ocr
        positional_char_set: PositionalCharacterSet = self._ocr.run(input_image)

        # run encipherer
        enciphered_positional_char_set: PositionalCharacterSet = self._encipherer.run(
            positional_char_set,
        )

        # run reconstructor
        reconstructed_image: ReconstructedImage = self._reconstructor.run(
            enciphered_positional_char_set, input_image,
        )

        # run output heads
        for output in self._outputs:
            output.run(reconstructed_image)
