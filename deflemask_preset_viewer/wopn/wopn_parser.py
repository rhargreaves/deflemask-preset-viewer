from .wopn import Wopn, WopnBank, WopnInstrument
from ..fm_operator import FmOperator


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
    for i in range(4):
        instrument.operators.append(read_operator(f))
    skip_over_delay_data(f)
    return instrument


def skip_over_delay_data(f):
    f.read(4)


def read_operator(f):
    op = FmOperator()
    detune_multiple_reg = int.from_bytes(
        f.read(1), byteorder='big', signed=False)
    op.mul = detune_multiple_reg & 0xf
    op.dt = detune_multiple_reg >> 4
    total_level_reg = int.from_bytes(
        f.read(1), byteorder='big', signed=False)
    op.tl = total_level_reg
    rate_scale_attack_reg = int.from_bytes(
        f.read(1), byteorder='big', signed=False)
    op.ar = rate_scale_attack_reg & 0x1f
    op.rs = rate_scale_attack_reg >> 6
    amplitude_first_decay_reg = int.from_bytes(
        f.read(1), byteorder='big', signed=False)
    op.am = amplitude_first_decay_reg >> 7
    op.dr = amplitude_first_decay_reg & 0x1f
    second_decay_rate_reg = int.from_bytes(
        f.read(1), byteorder='big', signed=False)
    op.d2r = second_decay_rate_reg
    sustain_level_and_release_rate_reg = int.from_bytes(
        f.read(1), byteorder='big', signed=False)
    op.sl = sustain_level_and_release_rate_reg >> 4
    op.rr = sustain_level_and_release_rate_reg & 0xf
    ssg_reg = int.from_bytes(
        f.read(1), byteorder='big', signed=False)
    op.ssg = ssg_reg
    return op


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
