from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="deflemask-preset-viewer",
    version="0.0.10",
    author="Robert Hargreaves",
    author_email="python-package@roberthargreaves.net",
    description="Reads and outputs FM parameters contained within DefleMask's DMP files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rhargreaves/deflemask-preset-viewer",
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    entry_points={
        "console_scripts": ['deflemask-preset-viewer = deflemask_preset_viewer.main:main']
    },
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Topic :: Multimedia :: Sound/Audio",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
