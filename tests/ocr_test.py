from typing import List

from PIL import Image
from PIL import ImageDraw

from ocr_cipher_solver.ocr import OCR


def run_ocr_with_img(img: Image.Image):
    """Tests OCR package provided example image."""
    # init OCR
    ocr = OCR()

    # run ocr on image
    charset = ocr.run(img)

    # display bounding boxes on images
    draw_img = ImageDraw.Draw(img)
    for char in charset:
        x0 = char.bounding_box.left
        y0 = img.height - char.bounding_box.top
        x1 = x0 + char.bounding_box.width
        y1 = y0 + char.bounding_box.height

        draw_img.rectangle((x0, y0, x1, y1))

    # display image
    img.show()

    # print character set
    print([char.character for char in charset])


def test_ocr_with_example_images(example_images: List[Image.Image]):
    """Tests OCR with example images."""
    for example_image in example_images:
        run_ocr_with_img(example_image)
        input()
