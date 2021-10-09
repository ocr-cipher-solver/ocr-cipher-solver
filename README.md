# ocr-cipher-solver
Implements an OCR cipher solver using optical character recognition and image augmentation.

## Build Instructions
You can install the `ocr-cipher-solver` package as follows:

```
python3 -m pip install --upgrade build
python3 -m build
python3 -m pip install -e .
```

## Development Instructions
Install pre-commit to ensure code quality.
```
pre-commit install
```

This will run checks on your code every time you commit.

## Test Instructions
You can run the test suite with the following command:

```
tox
```
