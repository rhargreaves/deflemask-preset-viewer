#!/usr/bin/env python3
import argparse
from parser import parse_file
from ui import print_dmp
from code import print_code


def main():
    print("DefleMask Preset Viewer")
    parser = argparse.ArgumentParser(description='View DMP details.')
    parser.add_argument('file')
    parser.add_argument(
        '-c',
        dest='c_code',
        help="Output as C code for the Mega Drive MIDI Interface project",
        action='store_true')
    args = parser.parse_args()
    dmp = parse_file(args.file)
    if args.c_code:
        print_code(dmp)
    else:
        print_dmp(dmp)


main()
