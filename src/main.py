#!/usr/bin/env python
import argparse
from collections import namedtuple

parser = argparse.ArgumentParser(description='View DMP details.')
parser.add_argument('file')
args = parser.parse_args()


def read_byte(file):
    return file.read(1)[0]


def main(args):
    with open(args.file, "rb") as f:
        version = read_byte(f)
        print("Version {}".format(version))

        if version == 8:
            instrument_mode = read_byte(f)
            system_type = None
        elif version == 11:
            system_type = read_byte(f)
            instrument_mode = read_byte(f)

    if instrument_mode == 1:
        print("FM")
    if system_type == 2:
        print("Genesis")


main(args)
