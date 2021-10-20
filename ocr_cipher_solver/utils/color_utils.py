import collections
from typing import DefaultDict
from typing import Dict
from typing import List
from typing import Tuple

from PIL import Image

from ocr_cipher_solver.data_formats import BoundingBox
from ocr_cipher_solver.data_formats import RGBA


def _downsample_rgba(color: RGBA, downsample_fac: int) -> RGBA:
    """Downsamples color.

    Parameters
    ----------
    color : RGBA
        color to downsample
    downsample_fac : int
        factor to downsample color by

    Returns
    -------
    RGBA
        downsampled color tuple
    """
    return (
        (color[0] // downsample_fac) * downsample_fac,
        (color[1] // downsample_fac) * downsample_fac,
        (color[2] // downsample_fac) * downsample_fac,
        (color[3] // downsample_fac) * downsample_fac,
    )


def _downsample_colors(colors: List[Tuple[int, RGBA]], downsample_fac: int) -> Dict[RGBA, int]:
    """Downsamples colors to smooth color spectrum

    Parameters
    ----------
    colors : List[Tuple[int, RGBA]]
        list of colors in image, with their number of instances
    downsample_fac : int
        factor to downsample colors by

    Returns
    -------
    Dict[RGBA, int]
        dictionary of downsampled colors and their number of occurrences
    """
    # downsample colors
    downsampled_colors = [
        (num_occurs, _downsample_rgba(color, downsample_fac))
        for num_occurs, color in colors
    ]

    # create histogram dictionary
    color_hist: DefaultDict[RGBA, int] = collections.defaultdict(int)
    for num_occurs, color in downsampled_colors:
        color_hist[color] += num_occurs

    # return histogram dict
    return dict(sorted(color_hist.items(), key=lambda x: x[1], reverse=True))


def _get_original_color(
    downsampled_color: RGBA,
    original_colors: List[Tuple[int, RGBA]],
    downsample_fac: int,
) -> RGBA:
    """Gets original color with most occurrences that maps into downsampled color.

    Parameters
    ----------
    downsampled_color : RGBA
        downsampled color to find mappings to
    original_colors : List[Tuple[int, RGBA]]
        original (non-downsampled) colors from image and their occurrences
    downsample_fac : int
        factor to downsample colors by (to check mappings)

    Returns
    -------
    RGBA
        original color that maps into downsampled color
    """
    # filter original colors to only ones that map into downsampled color
    matching_colors = [
        (num_occurrences, color)
        for num_occurrences, color in original_colors
        if _downsample_rgba(color, downsample_fac) == downsampled_color
    ]

    # get and return highest occurring original color maching the downsampled color
    return max(matching_colors, key=lambda x: x[0])[1]


def get_fg_bg_colors_from_img_section(
    img: Image.Image, bounding_box: BoundingBox, downsample_fac: int = 64,
) -> Tuple[RGBA, RGBA]:
    """Gets foreground (text) and background colors from image section.

    Parameters
    ----------
    img : Image.Image
        image to get colors from
    bounding_box : BoundingBox
        bounding box to look for colors within
    downsample_fac : float
        factor to downsample colors by (smooths colors)

    Returns
    -------
    Tuple[RGBA, RGBA]
        tuple of RGBA values for text color, background color
    """
    # get colors from image
    left, top, right, bottom = bounding_box.to_ltrb()
    colors: List[Tuple[int, RGBA]] = img.crop(
        (left, img.height - top, right, img.height - bottom),
    ).convert('RGBA').getcolors()   # type: ignore

    # downsample pixel values and get histogram
    downsampled_colors = _downsample_colors(colors, downsample_fac)

    # pick 1st and 2nd most common colors as fg, bg colors respectively
    fg, bg = [*downsampled_colors.keys()][:2]

    # map fg and bg back into original colors (most prevalent original color in subset)
    return (
        _get_original_color(fg, colors, downsample_fac),
        _get_original_color(bg, colors, downsample_fac),
    )
