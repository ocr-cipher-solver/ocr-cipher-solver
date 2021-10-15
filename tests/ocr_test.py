from PIL import Image
from PIL import ImageDraw

from ocr_cipher_solver.ocr import OCR


def test_ocr_with_covid_image():
    """Tests OCR package with covid example image."""
    # load image from file
    img = Image.open('./examples/covid.png')

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
