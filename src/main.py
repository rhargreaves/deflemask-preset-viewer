import argparse

parser = argparse.ArgumentParser(description='View DMP details.')
parser.add_argument('file')
args = parser.parse_args()

with open(args.file, "rb") as f:
    version = f.read(1)[0]
    instrument_mode = f.read(1)[0]

if instrument_mode == 1:
    print("FM")
