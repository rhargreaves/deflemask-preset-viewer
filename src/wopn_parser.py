from .preset import Preset


def parse_wopn(filename):
    p = Preset()
    with open(filename, "rb") as f:
        p.name = filename
        skip_magic_number(f)


def read_byte(file):
    return file.read(1)[0]


def skip_magic_number(f):
    for _ in range(11):
        read_byte(f)
