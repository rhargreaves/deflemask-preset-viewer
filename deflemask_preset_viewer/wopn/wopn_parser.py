from .wopn import Wopn
from collections import namedtuple


def parse_wopn(filename):
    p = Wopn()
    with open(filename, "rb") as f:
        p.name = filename
        p.magic_number = read_magic_number(f)
        if p.magic_number == 'WOPN2-B2NK':
            p.version = int.from_bytes(
                f.read(2), byteorder='little', signed=False)
        else:
            p.version = 1
        p.m_bank_count = int.from_bytes(
            f.read(2), byteorder='big', signed=False)
        p.p_bank_count = int.from_bytes(
            f.read(2), byteorder='big', signed=False)
        p.global_flags = int.from_bytes(f.read(1), byteorder='big')
        if p.version >= 2:
            p.m_banks = read_banks(p.m_bank_count, f)
            p.p_banks = read_banks(p.p_bank_count, f)
    return p


def read_banks(bank_count, f):
    banks = []
    for _ in range(bank_count):
        bank_name = f.read(32).decode('ascii').rstrip('\0')
        bank_index = int.from_bytes(
            f.read(2), byteorder='big', signed=False)
        Bank = namedtuple('Bank', 'name index')
        banks.append(Bank(bank_name, bank_index))
    return banks


def read_byte(file):
    return file.read(1)[0]


def read_magic_number(f):
    magic_number = f.read(10).decode('ascii').splitlines()[0]
    f.read(1)
    return magic_number
