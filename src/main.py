#!/usr/bin/env python3
import argparse
from .parser import parse_file
from .wopn_parser import parse_wopn
from .code import print_code


def main():
    args = parse_args()
    if args.file.lower().endswith('.wopn'):
        preset = parse_wopn(args.file)
    else:
        preset = parse_file(args.file)
    if args.c_code:
        print_code(preset)
    else:
        preset.print_info()


def parse_args():
    parser = argparse.ArgumentParser(description='View DMP details.')
    parser.add_argument('file')
    parser.add_argument(
        '-c',
        dest='c_code',
        help="Output as C code for the Mega Drive MIDI Interface project",
        action='store_true')
    return parser.parse_args()
