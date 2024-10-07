import os


def extract_name(path):
    return os.path.splitext(os.path.basename(path))[0]


def read_byte(file):
    return file.read(1)[0]
