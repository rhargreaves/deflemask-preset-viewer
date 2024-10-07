#!/usr/bin/env python3
import argparse
from .dmp.dmp_parser import parse_dmp
from .wopn.wopn_parser import parse_wopn
from .tfi.tfi_parser import parse_tfi
from .code import print_code


def main():
    args = parse_args()
    if args.file.lower().endswith('.wopn'):
        preset = parse_wopn(args.file)
    elif args.file.lower().endswith('.tfi'):
        preset = parse_tfi(args.file)
    else:
        preset = parse_dmp(args.file)
    if args.c_code:
        print_code(preset)
    else:
        print(preset.info())


def parse_args():
    parser = argparse.ArgumentParser(description='View preset details.')
    parser.add_argument('file')
    parser.add_argument(
        '-c',
        dest='c_code',
        help="Output as C code for the Mega Drive MIDI Interface project",
        action='store_true')
    return parser.parse_args()
