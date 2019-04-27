#!/usr/bin/env python3
import argparse
from parser import parse_file
from ui import print_dmp
from code import print_code


def main():
    args = parse_args()
    dmp = parse_file(args.file)
    if args.c_code:
        print_code(dmp, args.file)
    else:
        print_dmp(dmp)


def parse_args():
    parser = argparse.ArgumentParser(description='View DMP details.')
    parser.add_argument('file')
    parser.add_argument(
        '-c',
        dest='c_code',
        help="Output as C code for the Mega Drive MIDI Interface project",
        action='store_true')
    return parser.parse_args()


main()
