from typing import Dict
from typing import Tuple

from PIL import Image
from PIL import ImageDraw

from ocr_cipher_solver.data_formats import PositionalCharacterSet
from ocr_cipher_solver.data_formats.bounding_box import BoundingBox
from ocr_cipher_solver.data_formats.bounding_box import Coords
from ocr_cipher_solver.data_formats.positional_character import PositionalCharacter
from ocr_cipher_solver.utils.color_utils import get_fg_bg_colors_from_img_section
from ocr_cipher_solver.utils.font_utils import get_font_from_bounding_box


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
        reconstructed_img: Image.Image = input_image.copy()
        drawable_img: ImageDraw.ImageDraw = ImageDraw.Draw(reconstructed_img)
        for char in ciphered_char_set:
            self._draw_char(char, drawable_img, reconstructed_img.info)
#            self._draw_rect(char.bounding_box, drawable_img)

        return reconstructed_img

    @staticmethod
    def _draw_char(char: PositionalCharacter, drawable_img: ImageDraw.ImageDraw, img_info: Dict):
        """Draws character and returns resultant image.

        Parameters
        ----------
        char : PositionalCharacter
            positional character to draw on image
        drawable_img : ImageDraw.ImageDraw
            image to draw on
        img_info : Dict
            img information dict
        """
        # get colors for text, background
        # text_color, fill_color = get_fg_bg_colors_from_img_section(img, char.bounding_box)
        text_color, fill_color = (255, 255, 255, 255), (0, 0, 0, 255)

        # get font for character
        font = get_font_from_bounding_box(char.bounding_box, img_info.get('dpi', 72))

        # draw character on image and return
        drawable_img.text(
            char.bounding_box.to_ltrb(coords=Coords.TopLeft)[:2],
            char.character,
            font=font,
            fill=fill_color,
            stroke_fill=text_color,
        )

    @staticmethod
    def _draw_rect(bbox: BoundingBox, drawable_img: ImageDraw.ImageDraw):
        """Draws rectangle on image in bounding box.

        Parameters
        ----------
        bbox : BoundingBox
            bounding box to draw rect in
        drawable_img : ImageDraw.ImageDraw
            image to draw rect onto
        """
        fill_color = (0, 0, 0, 255)

        drawable_img.rectangle(
            bbox.to_ltrb(coords=Coords.TopLeft),
            fill=fill_color,
        )
