#!/usr/bin/env python
import argparse
from collections import namedtuple

parser = argparse.ArgumentParser(description='View DMP details.')
parser.add_argument('file')
args = parser.parse_args()


class Dmp:
    def __init__(self):
        self.version = None
        self.system_type = None
        self.instrument_mode = None
        self.lfo_fms = None
        self.lfo_ams = None
        self.feedback = None
        self.algorithm = None


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
    return dmp


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
    if dmp.system_type == 2:
        print("Genesis")


main(args)
