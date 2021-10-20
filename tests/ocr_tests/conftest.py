import pathlib
from typing import Generator
from typing import List

import pytest
from PIL import Image


@pytest.fixture
def example_images() -> Generator[List[Image.Image], None, None]:
    """Returns a list of example images."""
    # get list of image paths in examples directory
    file_extensions = ('png', 'jpg', 'jpeg')
    img_paths = [
        path
        for ext in file_extensions
        for path in pathlib.Path('./examples/').glob(f'*.{ext}')
    ]

    # yield opened image files
    images = [Image.open(img_path) for img_path in img_paths]
    yield images

    # close image files
    for image in images:
        image.close()
