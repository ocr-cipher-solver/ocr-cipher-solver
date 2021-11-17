import pathlib

from PIL import Image

from ocr_cipher_solver.ciphers import CaesarianCipher
from ocr_cipher_solver.ocr import OCR
from ocr_cipher_solver.pipeline import ImagePipeline
from ocr_cipher_solver.reconstructor import Reconstructor


if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(prog='OCR Cipher Solver')

    parser.add_argument('img_path', type=pathlib.Path)
    parser.add_argument('--shift', type=int, default=0)

    args = parser.parse_args()

    # initialize pipeline
    pipeline = ImagePipeline(
        OCR(),
        CaesarianCipher(shift=args.shift),
        Reconstructor(),
        (),
    )

    # run pipeline
    pipeline.run_pipeline(Image.open(args.img_path))
