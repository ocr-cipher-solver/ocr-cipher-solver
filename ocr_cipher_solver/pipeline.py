"""Defines the image processing pipeline."""
from typing import Tuple

from PIL import Image

from .ciphers import Encipherer
from .ciphers import EnciphererResult
from .ocr import OCR
from .ocr import OCRResult
from .outputs import PipelineOutput
from .reconstructor import Reconstructor
from .reconstructor import ReconstructorResult


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

    def run_pipeline(self, img: Image.Image):
        """Runs pipeline, feeding results forward through stages.

        Parameters
        ----------
        img : Image.Image
            img to run pipeline with
        """
        # run ocr
        ocr_result: OCRResult = self._ocr.run(img)

        # run encipherer
        encipherer_result: EnciphererResult = self._encipherer.run(ocr_result)

        # run reconstructor
        reconstructor_result: ReconstructorResult = self._reconstructor.run(encipherer_result, img)

        # run output heads
        for output in self._outputs:
            output.run(reconstructor_result)
