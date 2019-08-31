from .wopn import Wopn, WopnBank, WopnInstrument


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
        global_lfo_reg = int.from_bytes(f.read(1), byteorder='big')
        p.lfo_enable = bool(global_lfo_reg >> 3)
        p.lfo_freq = (global_lfo_reg & 0x7)
        if p.version >= 2:
            p.m_banks = read_banks(p.m_bank_count, f)
            p.p_banks = read_banks(p.p_bank_count, f)
        for bank in p.m_banks:
            for _ in range(128):
                bank.instruments.append(read_instrument(f))
        for bank in p.p_banks:
            for _ in range(128):
                bank.instruments.append(read_instrument(f))
    return p


def read_instrument(f):
    instrument = WopnInstrument()
    instrument.name = f.read(32).decode('ascii').rstrip('\0')
    instrument.key_offset = int.from_bytes(
        f.read(2), byteorder='big', signed=False)
    instrument.percussion_key = int.from_bytes(
        f.read(1), byteorder='big', signed=False)
    feedback_algorithm_reg = int.from_bytes(
        f.read(1), byteorder='big', signed=False)
    instrument.algorithm = feedback_algorithm_reg & 0x7
    instrument.feedback = feedback_algorithm_reg >> 3
    stereo_lfo_reg = int.from_bytes(
        f.read(1), byteorder='big', signed=False)
    instrument.lfo_ams = stereo_lfo_reg >> 3
    instrument.lfo_fms = stereo_lfo_reg & 0x7

    f.read(7 * 4)  # ops
    f.read(4)  # delay
    return instrument


def read_banks(bank_count, f):
    banks = []
    for _ in range(bank_count):
        bank_name = f.read(32).decode('ascii').rstrip('\0')
        bank_index = int.from_bytes(
            f.read(2), byteorder='big', signed=False)
        banks.append(WopnBank(bank_name, bank_index))
    return banks


def read_byte(file):
    return file.read(1)[0]


def read_magic_number(f):
    magic_number = f.read(10).decode('ascii').splitlines()[0]
    f.read(1)
    return magic_number
