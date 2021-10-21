import collections
from typing import DefaultDict
from typing import Dict
from typing import List
from typing import Tuple

from PIL import Image
from PIL import ImageChops
from PIL import ImageFilter
from PIL import ImageOps

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


def _invert_mask(mask: Image.Image) -> Image.Image:
    """Inverts mask.

    Parameters
    ----------
    mask : Image.Image
        mask to invert

    Returns
    -------
    Image.Image
        inverted image mask
    """
    return ImageOps.invert(mask.convert('L')).convert('1')


def _get_text_mask(img: Image.Image, kernel_size_fac: float, pixel_thresh: int) -> Image.Image:
    """Gets text mask using high-pass filter.

    Parameters
    ----------
    img : Image.Image
        image to get text mask for
    kernel_size_fac : float
        factor of the size of the smallest dimension of the image to use for Gaussian kernel
    pixel_thresh : int
        pixel lut threshold to include in text mask (lower -> more sensitive)

    Returns
    -------
    Image.Image
        text mask constructed from image
    """
    # find kernel size (factor of the size of the smallest dimension of the image)
    kernel_size = int(kernel_size_fac * min(img.width, img.height))

    # get difference between image and smoothed image
    raw_diff = ImageChops.difference(
        img, img.filter(ImageFilter.GaussianBlur(radius=kernel_size)),
    )

    # threshold, convert to binary, and return image
    return raw_diff.convert('L').point(lambda p: p > pixel_thresh and 256, mode='1')


def _mask_image(img: Image.Image, mask: Image.Image) -> Image.Image:
    """Masks image with provided mask.

    Parameters
    ----------
    img : Image.Image
        image to mask
    mask : Image.Image
        mask to mask image with

    Returns
    -------
    Image.Image
        masked image
    """
    return Image.composite(
        img.convert('RGB'),
        Image.new('RGB', (img.width, img.height), (0, 0, 0, 255)),
        mask,
    ).convert('RGBA')


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
    # crop image to character
    left, top, right, bottom = bounding_box.to_ltrb()
    cropped_img: Image.Image = img.crop(
        (left, img.height - top, right, img.height - bottom),
    ).convert('RGBA')

    # get foreground and background masked images
    text_mask: Image.Image = _get_text_mask(cropped_img, kernel_size_fac=0.05, pixel_thresh=64)
    fg_img: Image.Image = _mask_image(cropped_img, text_mask)
    bg_img: Image.Image = _mask_image(cropped_img, _invert_mask(text_mask))

    # get colors for foreground, background masked images
    fg_colors: List[Tuple[int, RGBA]] = fg_img.getcolors()  # type: ignore
    bg_colors: List[Tuple[int, RGBA]] = bg_img.getcolors()  # type: ignore

    # downsample pixel values and get histogram
    downsampled_fg_colors = _downsample_colors(fg_colors, downsample_fac)
    downsampled_bg_colors = _downsample_colors(bg_colors, downsample_fac)

    # pick the most common colors for fg, bg
    fg: RGBA = next(iter(downsampled_fg_colors))
    bg: RGBA = next(iter(downsampled_bg_colors))

    # map fg and bg back into original colors (most prevalent original color in subset)
    return (
        _get_original_color(fg, fg_colors, downsample_fac),
        _get_original_color(bg, bg_colors, downsample_fac),
    )
