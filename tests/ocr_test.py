from PIL import Image

from ocr_cipher_solver.ocr import OCR


def test_ocr_with_covid_image():
    """Tests OCR package with covid example image."""
    # load image from file
    img = Image.open('./examples/covid.png')

    # init OCR
    ocr = OCR()

    # run ocr on image
    charset = ocr.run(img)
