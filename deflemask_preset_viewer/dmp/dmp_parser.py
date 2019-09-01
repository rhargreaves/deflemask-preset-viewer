from .dmp import Dmp
from ..fm_operator import FmOperator
from bitstruct import unpack


def read_byte(file):
    return file.read(1)[0]


def parse_dmp(filename):
    dmp = Dmp()
    with open(filename, "rb") as f:
        dmp.name = filename
        dmp.version = read_byte(f)
        if dmp.version == 8:
            dmp.instrument_mode = read_byte(f)
            read_byte(f)  # unknown
        elif dmp.version == 11:
            dmp.system_type = read_byte(f)
            dmp.instrument_mode = read_byte(f)
        if dmp.instrument_mode == 1:
            dmp.lfo_fms = read_byte(f)
            dmp.feedback = read_byte(f)
            dmp.algorithm = read_byte(f)
            dmp.lfo_ams = read_byte(f)
            ops = []
            for _ in range(4):
                ops.append(parse_operator(f))
            dmp.operators.append(ops[0])
            dmp.operators.append(ops[2])
            dmp.operators.append(ops[1])
            dmp.operators.append(ops[3])
    return dmp


def parse_operator(f):
    mul, tl, ar, dr, sl, rr, am, rs, dt, d2r, ssg = unpack(
        'u8u8u8u8u8u8u8u8u8u8u8', f.read(11))
    return FmOperator(dt, mul, tl, rs, ar, am, dr, d2r, sl, rr, ssg)
