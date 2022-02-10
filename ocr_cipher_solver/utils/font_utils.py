import functools

from PIL import ImageFont

from ocr_cipher_solver.data_formats import BoundingBox


@functools.lru_cache(maxsize=256)
def _char_width(font: ImageFont.FreeTypeFont, char: str) -> float:
    """Finds character width (in pixels) for a given font.

    Parameters
    ----------
    font : ImageFont.FreeTypeFont
        font to find avg char width for
    char : str
        character to use

    Returns
    -------
    float
        character width in pixels
    """
    return font.getsize(char)[0]


@functools.lru_cache(maxsize=256)
def get_font_from_bounding_box(width: int, char: str) -> ImageFont.FreeTypeFont:
    """Gets font from bounding box width.

    Parameters
    ----------
    width : int
        width of bounding box
    char : str
        character to use

    Returns
    -------
    ImageFont.FreeTypeFont
        font object created for character
    """
    # find font that best fit bounding box width
    best_font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 1)

    for font_size in range(2, 128):
        font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', font_size)
        if _char_width(font, char) < width:
            best_font = font
        else:
            break

    return best_font
