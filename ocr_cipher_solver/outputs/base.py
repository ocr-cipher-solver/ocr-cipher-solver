import abc

from PIL import Image


class PipelineOutput(abc.ABC):
    """Pipeline output base class."""
    @abc.abstractmethod
    def run(self, output_image: Image.Image):
        """Runs output operation on output image.

        Parameters
        ----------
        output_image : Image.Image
            image to run output operation on
        """
        raise NotImplementedError
