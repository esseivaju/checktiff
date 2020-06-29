# checktiff
Tool to check exif tag of a TIF image database. The script walks through a specified directory and for each  TIF file found it wil check that a preconfigured list of Metadata / EXIF tags exist.

## Setup

Checktiff requires python 3.7 and should be installed in a virtual environment.

```bash
pip install .
```

## Usage

```bash
usage: check_tiff [-h] -d DATA_PATH [-e] -o OUTPUT_FILE

optional arguments:
  -h, --help            show this help message and exit
  -e, --enable-optional
                        Enable checking of One-Shot systems metadata

required arguments:
  -d DATA_PATH, --data-path DATA_PATH
                        Directory to check
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        Output summary file
```
