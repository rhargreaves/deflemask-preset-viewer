#!/usr/bin/env python3
import argparse
from collections import namedtuple

parser = argparse.ArgumentParser(description='View DMP details.')
parser.add_argument('file')
args = parser.parse_args()


class Operator:
    def __init__(self):
        self.mul = None
        self.tl = None
        self.ar = None
        self.dr = None
        self.sl = None
        self.rr = None
        self.am = None
        self.rs = None
        self.dt = None
        self.d2r = None
        self.ssg = None


class Dmp:
    def __init__(self):
        self.version = None
        self.system_type = None
        self.instrument_mode = None
        self.lfo_fms = None
        self.lfo_ams = None
        self.feedback = None
        self.algorithm = None
        self.operators = []


def read_byte(file):
    return file.read(1)[0]


def parse_file(filename):
    dmp = Dmp()
    with open(filename, "rb") as f:
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
            for i in range(4):
                dmp.operators.append(parse_operator(f))
    return dmp


def parse_operator(f):
    op = Operator()
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


def print_op(name, value_func, operators):
    print(name, end='')
    for i in [0, 2, 1, 3]:
        op = operators[i]
        print("\t{}".format(value_func(op)), end='')
    print()


def print_operator_headers():
    print("Operator", end='')
    for i in range(4):
        print("\t{}".format(i+1), end='')
    print()


def format_instrument_mode(mode):
    return "FM" if mode == 1 else "STD"


def format_system(system_type):
    return "Genesis" if system_type == 2 else "Unknown"


def print_type(dmp):
    print("Version  {0: <2}      {1: <3}      {2: <7}".format(
        dmp.version,
        format_instrument_mode(dmp.instrument_mode),
        format_system(dmp.system_type)))


def main(args):
    dmp = parse_file(args.file)
    print_type(dmp)
    if dmp.instrument_mode == 1:
        print("Algorithm  {}     LFO FMS  {}".format(dmp.algorithm, dmp.lfo_fms))
        print("Feedback   {}     LFO AMS  {}".format(dmp.feedback, dmp.lfo_ams))
        print_operator_headers()
        print_op("MUL", lambda op: op.mul, dmp.operators)
        print_op("TL", lambda op: op.tl, dmp.operators)
        print_op("AR", lambda op: op.ar, dmp.operators)
        print_op("DR", lambda op: op.dr, dmp.operators)
        print_op("SL", lambda op: op.sl, dmp.operators)
        print_op("RR", lambda op: op.rr, dmp.operators)
        print_op("AM", lambda op: op.am, dmp.operators)
        print_op("RS", lambda op: op.rs, dmp.operators)
        print_op("DT", lambda op: op.dt, dmp.operators)
        print_op("D2R", lambda op: op.d2r, dmp.operators)
        print_op("SSG", lambda op: op.ssg, dmp.operators)


main(args)
