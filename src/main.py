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
    read_byte(f)
    read_byte(f)
    read_byte(f)
    read_byte(f)
    read_byte(f)
    read_byte(f)
    read_byte(f)
    return op


def print_op(name, value_func, operators):
    print(name, end='')
    for i in [0, 2, 1, 3]:
        op = operators[i]
        print("\t{}".format(value_func(op)), end='')
    print()


def main(args):
    dmp = parse_file(args.file)
    print("Version {}".format(dmp.version))
    if dmp.instrument_mode == 1:
        print("FM")
        if dmp.lfo_fms is not None:
            print("LFO FMS 0x{:02X}".format(dmp.lfo_fms))
        if dmp.lfo_ams is not None:
            print("LFO AMS 0x{:02X}".format(dmp.lfo_ams))
        if dmp.feedback is not None:
            print("Feedback 0x{:02X}".format(dmp.feedback))
        if dmp.feedback is not None:
            print("Algorithm 0x{:02X}".format(dmp.algorithm))
        print("Operator", end='')
        for i in range(4):
            print("\t{}".format(i+1), end='')
        print()
        print_op("MUL", lambda op: op.mul, dmp.operators)
        print_op("TL", lambda op: op.tl, dmp.operators)
        print_op("AR", lambda op: op.ar, dmp.operators)
        print_op("DR", lambda op: op.dr, dmp.operators)
    if dmp.system_type == 2:
        print("Genesis")


main(args)
