# DefleMask Preset Viewer [![CircleCI](https://circleci.com/gh/rhargreaves/deflemask-preset-viewer.svg?style=svg)](https://circleci.com/gh/rhargreaves/deflemask-preset-viewer) [![PyPI version](https://badge.fury.io/py/deflemask-preset-viewer.svg)](https://badge.fury.io/py/deflemask-preset-viewer)

Reads Deflemask preset files (DMP) and displays the stored parameters. Also supports dumping of bank and instrument data of [WOPN files](https://github.com/Wohlstand/libOPNMIDI/blob/master/fm_banks/wopn%20specification.txt) as used by [libOPNMIDI](https://github.com/Wohlstand/libOPNMIDI)

## Supported Formats

- DefleMask preset versions 8 and 11
- WOPN versions 1 and 2

## Installation

```
$ pip3 install deflemask-preset-viewer
```

## Usage

### DMP files

```sh
$ deflemask-preset-viewer deflemask_preset_viewer/tests/data/sample.dmp
Version    8       FM       Unknown
Algorithm  3       LFO FMS  0
Feedback   0       LFO AMS  0
------------------------------------------------------------
Operator   1       2       3       4
------------------------------------------------------------
MUL        14      1       0       0
TL         39      24      24      19
AR         31      31      31      31
D1R        15      14      9       9
D1L        14      14      14      14
RR         15      15      15      15
AM         0       0       0       0
RS         2       0       0       0
DT1        3       3       3       3
D2R        0       0       0       0
SSG        0       0       0       0
```

### WOPN files

```sh
$ deflemask_preset_viewer deflemask_preset_viewer/tests/data/sample.wopn
WOPN
M_Banks    2
P_Banks    5
LFO       On
LFO Freq   1
============================================================
M. Bank       0    Standard :3
============================================================
============================================================
Instrument    0    * GrandPiano
============================================================
Algorithm  2       LFO FMS  0
Feedback   0       LFO AMS  0
------------------------------------------------------------
Operator   1       2       3       4
------------------------------------------------------------
MUL        1       4       2       1
TL         39      36      4       2
AR         26      24      31      27
D1R        7       9       23      4
D1L        7       6       9       10
RR         1       7       1       6
AM         0       0       0       0
RS         1       1       3       2
DT1        0       6       7       3
D2R        4       9       15      4
SSG        0       0       0       0
============================================================
Instrument    1    * BrightPiano
============================================================
Algorithm  5       LFO FMS  0
Feedback   7       LFO AMS  0
...
```

It can also generate C code for inclusion in the [Mega Drive MIDI Interface](https://github.com/rhargreaves/mega-drive-midi-interface) project. Specify `-c` to output parameters in this way:

```sh
$ deflemask-preset-viewer deflemask_preset_viewer/tests/data/sample.dmp -c
static const Channel SAMPLE = { 3, 0, 3, 0, 0, 0, 0,
    { 14, 3, 31, 2, 15, 0, 14, 0, 15, 39, 0 },
    { 1, 3, 31, 0, 14, 0, 14, 0, 15, 24, 0 },
    { 0, 3, 31, 0, 9, 0, 14, 0, 15, 24, 0 },
    { 0, 3, 31, 0, 9, 0, 14, 0, 15, 19, 0 } };
```

## Build & Test

```sh
$ make test
```
