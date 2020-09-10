# checktiff
Tool to check exif tag of a TIF image database. The script walks through a specified directory and for each  TIF file found it wil check that a preconfigured list of Metadata / EXIF tags exist on each file. It will output missing tags in the log file

TAGS can be added / removed in the REQUIRED_TAGS and OPTIONAL_TAGS sets in bin/check_tiff if needed

## Setup

Checktiff requires python 3.7 and should be installed in a virtual environment.

```bash
conda create -nchecktiff python=3.7
conda activate checktiff
pip install .
check_tiff --help
```

## Example 
The command below will check that all tif files presentin ```/path/to/root/data/dir``` and its subdirectory have the required and optional exif tags.


```bash
check_tiff --enable-optional -d /path/to/root/data/dir -o output.log
```

## Usage

```bash
usage: check_tiff [-h] -d DATA_PATH [-e] -o OUTPUT_FILE

optional arguments:
  -h, --help            show this help message and exit
  -e, --enable-optional
                        Enable checking of optional One-Shot systems metadata

required arguments:
  -d DATA_PATH, --data-path DATA_PATH
                        Directory to check
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        Output summary file. Default to check_tiff.log in the current dir
```
