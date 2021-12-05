import pathlib
import subprocess


def encipher_img(img_fp: pathlib.Path, shift: int):
    save_path = img_fp.parent.joinpath(pathlib.Path(img_fp.name.rsplit(".", maxsplit=1)[0] + f"_enciphered_{shift}" + ".png"))
    subprocess.run(
        ["python", "-m", "ocr_cipher_solver", str(img_fp), "--shift", str(shift), "--save_path", str(save_path)]
    )


if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(prog='OCR Cipher Solver -- RUn All Images')

    parser.add_argument('img_dir', type=pathlib.Path)
    parser.add_argument('--shift', type=int, default=0)

    args = parser.parse_args()

    for img_fp in args.img_dir.glob("*"):
        if "enciphered" not in str(img_fp):
            print(img_fp)
            encipher_img(img_fp, args.shift)
