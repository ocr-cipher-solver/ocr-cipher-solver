from typing import Tuple

import pytest
from PIL import Image

from .conftest import expected_colors
from .conftest import test_bounding_boxes
from .conftest import test_img_paths
from ocr_cipher_solver.data_formats import BoundingBox
from ocr_cipher_solver.data_formats import RGBA
from ocr_cipher_solver.utils import get_fg_bg_colors_from_img_section


@pytest.mark.parametrize(
    ('test_img', 'bounding_box', 'expected_color'),
    zip(test_img_paths, test_bounding_boxes, expected_colors),
    indirect=True,
)
def test_get_fg_bg_colors_from_img_section(
    test_img: Image.Image, bounding_box: BoundingBox, expected_color: Tuple[RGBA, RGBA],
):
    """Tests getting FG and BG colors from image section."""
    # get foreground and background colors
    fg, bg = get_fg_bg_colors_from_img_section(test_img, bounding_box)

    # check that colors are as expected
    expected_fg, expected_bg = expected_color
    assert fg == expected_fg, f'FG color {fg} not what was expected {expected_fg}.'
    assert bg == expected_bg, f'FG color {bg} not what was expected {expected_bg}.'
