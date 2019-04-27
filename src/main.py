#!/usr/bin/env python3
import argparse
from colorama import Fore, Back, Style
from parser import parse_file
from ui import print_dmp


def main():
    print("DefleMask Preset Viewer")
    parser = argparse.ArgumentParser(description='View DMP details.')
    parser.add_argument('file')
    args = parser.parse_args()
    dmp = parse_file(args.file)
    print_dmp(dmp)


main()
