import pathlib
from typing import List
from typing import Tuple

import pytest
from PIL import Image

from ocr_cipher_solver.data_formats import BoundingBox
from ocr_cipher_solver.data_formats import RGBA


test_img_paths: List[pathlib.Path] = [
    pathlib.Path('./examples/covid.png'),
    pathlib.Path('./examples/oldmagazine_1.png'),
    pathlib.Path('./examples/magazine_2.png'),
]

test_bounding_boxes: List[BoundingBox] = [
    BoundingBox(236, 442, 12, 18),
    BoundingBox(183, 758, 6, 9),
    BoundingBox(309, 1169, 92, 95),
]

expected_colors: List[Tuple[RGBA, RGBA]] = [
    ((255, 255, 255, 255), (0, 152, 203, 255)),
    ((1, 1, 1, 255), (255, 255, 255, 255)),
    ((204, 60, 61, 255), (255, 255, 255, 255)),
]


@pytest.fixture(params=test_img_paths)
def test_img(request):
    return Image.open(request.param)


@pytest.fixture(params=test_bounding_boxes)
def bounding_box(request):
    return request.param


@pytest.fixture(params=expected_colors)
def expected_color(request):
    return request.param
