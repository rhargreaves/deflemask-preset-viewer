#!/usr/bin/env python
import argparse
from collections import namedtuple

parser = argparse.ArgumentParser(description='View DMP details.')
parser.add_argument('file')
args = parser.parse_args()


def read_byte(file):
    return file.read(1)[0]


def parse_file(filename):
    pass


def main(args):
    dmp_info = namedtuple("DmpInfo", "version system_type instrument_mode")
    with open(args.file, "rb") as f:

        dmp_info.version = read_byte(f)

        if dmp_info.version == 8:
            dmp_info.instrument_mode = read_byte(f)
            dmp_info.system_type = None
        elif dmp_info.version == 11:
            dmp_info.system_type = read_byte(f)
            dmp_info.instrument_mode = read_byte(f)

    print("Version {}".format(dmp_info.version))
    if dmp_info.instrument_mode == 1:
        print("FM")
    if dmp_info.system_type == 2:
        print("Genesis")


main(args)
