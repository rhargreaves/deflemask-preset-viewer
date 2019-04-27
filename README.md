# DefleMask Preset Viewer [![CircleCI](https://circleci.com/gh/rhargreaves/deflemask-preset-viewer.svg?style=svg)](https://circleci.com/gh/rhargreaves/deflemask-preset-viewer)
Reads DMP files and displays the stored parameters

## Usage

```sh
$ python3 src/main tests/sample.dmp
DefleMask Preset Viewer
Version    8       FM       Unknown
Algorithm  3       LFO FMS  0
Feedback   0       LFO AMS  0
Operator   1       2       3       4
MUL        14      1       0       0
TL         39      24      24      19
AR         31      31      31      31
DR         15      14      9       9
SL         14      14      14      14
RR         15      15      15      15
AM         0       0       0       0
RS         2       0       0       0
DT         3       3       3       3
D2R        0       0       0       0
SSG        0       0       0       0
```

## Supported Versions

Only supports 8 and 11 versions of the DMP format.

## Build & Test

```sh
$ make test
```
