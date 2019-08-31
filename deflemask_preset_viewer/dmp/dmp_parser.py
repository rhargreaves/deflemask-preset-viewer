from .dmp import Dmp
from ..fm_operator import FmOperator


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
    op = FmOperator()
    op.mul = read_byte(f)
    op.tl = read_byte(f)
    op.ar = read_byte(f)
    op.dr = read_byte(f)
    op.sl = read_byte(f)
    op.rr = read_byte(f)
    op.am = read_byte(f)
    op.rs = read_byte(f)
    op.dt = read_byte(f)
    op.d2r = read_byte(f)
    op.ssg = read_byte(f)
    return op
