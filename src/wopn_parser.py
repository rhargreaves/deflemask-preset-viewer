from .wopn import Wopn


def parse_wopn(filename):
    p = Wopn()
    with open(filename, "rb") as f:
        p.name = filename
        p.magic_number = read_magic_number(f)
        if p.magic_number == 'WOPN2-B2NK':
            p.version = 2
        else:
            p.version = 1
    return p


def read_byte(file):
    return file.read(1)[0]


def read_magic_number(f):
    magic_number = f.read(10).decode('ascii').splitlines()[0]
    f.read(1)
    return magic_number
