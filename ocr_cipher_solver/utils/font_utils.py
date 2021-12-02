import functools
import string
import time

from PIL import ImageFont

from ocr_cipher_solver.data_formats import BoundingBox


@functools.lru_cache(maxsize=256)
def _avg_char_width(font: ImageFont.FreeTypeFont) -> float:
    """Finds average character width (in pixels) for a given font.

    Parameters
    ----------
    font : ImageFont.FreeTypeFont
        font to find avg char width for

    Returns
    -------
    float
        average character width in pixels
    """
    return sum(font.getsize(char)[0] for char in string.ascii_letters) / len(string.ascii_letters)


@functools.lru_cache(maxsize=256)
def get_font_from_bounding_box(width: int) -> ImageFont.FreeTypeFont:
    """Gets font from bounding box width.

    Parameters
    ----------
    width : int
        width of bounding box

    Returns
    -------
    ImageFont.FreeTypeFont
        font object created for character
    """
    # find font that best fit bounding box width
    best_font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 1)

    tic = time.time()
    for font_size in range(2, 128):
        font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', font_size)
        if _avg_char_width(font) < width:
            best_font = font
        else:
            break

    print(f'{time.time() - tic}')

    return best_font
