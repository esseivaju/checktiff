from setuptools import setup, find_packages

setup(
    name="Checktiff",
    author="Julien Esseiva",
    description="Tool to check exif tag of a TIF image database",
    version="0.1",
    packages=find_packages(),
    scripts=["bin/check_tiff"],
    install_requires=[
        "Pillow>=7.1.2"
    ]
)