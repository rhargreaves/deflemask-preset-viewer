#!/usr/bin/env python
import argparse
from collections import namedtuple

parser = argparse.ArgumentParser(description='View DMP details.')
parser.add_argument('file')
args = parser.parse_args()


class Dmp:
    def __init__(self):
        self.veversion = None
        self.system_type = None
        self.instrument_mode = None
        self.lfo = None


def read_byte(file):
    return file.read(1)[0]


def parse_file(filename):
    dmp = Dmp()
    with open(filename, "rb") as f:
        dmp.version = read_byte(f)
        if dmp.version == 8:
            dmp.instrument_mode = read_byte(f)
        elif dmp.version == 11:
            dmp.system_type = read_byte(f)
            dmp.instrument_mode = read_byte(f)
        if dmp.instrument_mode == 1:
            dmp.lfo = read_byte(f)
    return dmp


def main(args):
    dmp = parse_file(args.file)
    print("Version {}".format(dmp.version))
    if dmp.instrument_mode == 1:
        print("FM")
        if dmp.lfo is not None:
            print("LFO 0x{:02X}".format(dmp.lfo))
    if dmp.system_type == 2:
        print("Genesis")


main(args)
