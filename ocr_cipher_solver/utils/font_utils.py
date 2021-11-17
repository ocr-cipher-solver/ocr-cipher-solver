from PIL import ImageFont

from ocr_cipher_solver.data_formats import BoundingBox


def get_font_from_bounding_box(bbox: BoundingBox, dpi: int) -> ImageFont.FreeTypeFont:
    """Gets font from bounding box.

    Parameters
    ----------
    bbox : BoundingBox
        bounding box for character

    dpi : int
        density of pixels in image

    Returns
    -------
    ImageFont.FreeTypeFont
        font object created for character
    """
    # get font size in pixels
    font_size_in_pixels = int(bbox.width * dpi / 96)

    # create and return ttf font
    return ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', font_size_in_pixels)
