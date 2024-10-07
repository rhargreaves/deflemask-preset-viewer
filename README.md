# DefleMask Preset Viewer [![Build and Release](https://github.com/rhargreaves/deflemask-preset-viewer/actions/workflows/build.yml/badge.svg)](https://github.com/rhargreaves/deflemask-preset-viewer/actions/workflows/build.yml) [![PyPI version](https://badge.fury.io/py/deflemask-preset-viewer.svg)](https://badge.fury.io/py/deflemask-preset-viewer)

Reads VGM preset files (including DefleMask, WOPN & TFI) and displays the stored parameters.

## Supported Formats

- DefleMask preset versions 8, 9 and 11
- [WOPN](https://github.com/Wohlstand/libOPNMIDI/blob/master/fm_banks/wopn%20specification.txt) versions 1 and 2, as used by libOPNMIDI
- [TFI](https://vgmrips.net/wiki/TFI_File_Format)

## Installation

```
$ pip3 install deflemask-preset-viewer
```

## Usage

### Output Parameters to Console

#### DMP files

```sh
$ deflemask-preset-viewer deflemask_preset_viewer/tests/data/sample.dmp
Version    8       FM       Unknown
Algorithm  3       LFO FMS  0
Feedback   0       LFO AMS  0
------------------------------------------------------------
Parameter  Op 1    Op 2    Op 3    Op 4
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

#### WOPN files

```sh
$ deflemask-preset-viewer deflemask_preset_viewer/tests/data/sample.wopn
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
Parameter  Op 1    Op 2    Op 3    Op 4
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
------------------------------------------------------------
...
```

#### TFI files

```sh
$ deflemask-preset-viewer deflemask_preset_viewer/tests/data/sample.tfi
Algorithm  4       LFO FMS  0
Feedback   7       LFO AMS  0
------------------------------------------------------------
Parameter  Op 1    Op 2    Op 3    Op 4
------------------------------------------------------------
MUL        2       1       2       1
TL         33      15      33      15
AR         31      31      31      31
D1R        0       0       0       0
D1L        0       0       0       0
RR         15      15      15      15
AM         0       0       0       0
RS         0       0       0       0
DT1        6       6       0       0
D2R        0       0       0       0
SSG        0       0       0       0
```

### Output as C Code

It can also generate C code for inclusion in the [Mega Drive MIDI Interface](https://github.com/rhargreaves/mega-drive-midi-interface) project. Specify `-c` to output parameters in this way:

#### DMP & TFI files

```sh
$ deflemask-preset-viewer deflemask_preset_viewer/tests/data/sample.dmp -c
static const Channel SAMPLE = { 3, 0, 3, 0, 0, 0, 0,
    { 14, 3, 31, 2, 15, 0, 14, 0, 15, 39, 0 },
    { 1, 3, 31, 0, 14, 0, 14, 0, 15, 24, 0 },
    { 0, 3, 31, 0, 9, 0, 14, 0, 15, 24, 0 },
    { 0, 3, 31, 0, 9, 0, 14, 0, 15, 19, 0 } };
```

#### WOPN files

```sh
$ deflemask-preset-viewer deflemask_preset_viewer/tests/data/sample.wopn -c
static const Channel M_BANK_0_INST_0_GRANDPIANO = { 2, 0, 3, 0, 0, 0, 0, {
    { 1, 0, 26, 1, 7, 0, 7, 4, 1, 39, 0 },
    { 4, 6, 24, 1, 9, 0, 6, 9, 7, 36, 0 },
    { 2, 7, 31, 3, 23, 0, 9, 15, 1, 4, 0 },
    { 1, 3, 27, 2, 4, 0, 10, 4, 6, 2, 0 } } };

static const Channel M_BANK_0_INST_1_BRIGHTPIANO = { 5, 7, 3, 0, 0, 0, 0, {
    { 4, 2, 27, 1, 9, 0, 11, 5, 6, 33, 0 },
    { 4, 5, 27, 1, 9, 0, 7, 9, 7, 18, 0 },
    { 1, 2, 27, 1, 5, 1, 10, 5, 6, 8, 0 },
    { 6, 5, 27, 1, 9, 0, 3, 8, 7, 9, 0 } } };

...
static const Channel M_BANK_0_INST_127_GUNSHOT = { 5, 7, 3, 0, 1, 0, 0, {
    { 3, 3, 31, 0, 3, 0, 15, 17, 5, 4, 0 },
    { 1, 0, 31, 0, 20, 0, 15, 20, 8, 0, 0 },
    { 1, 0, 31, 0, 15, 0, 15, 31, 8, 0, 0 },
    { 1, 0, 31, 0, 15, 0, 15, 16, 11, 0, 0 } } };

static const Channel M_BANK_0[] = {
    M_BANK_0_INST_0_GRANDPIANO,
    M_BANK_0_INST_1_BRIGHTPIANO,
...
    M_BANK_0_INST_127_GUNSHOT
};
```

## Build & Test

```sh
$ make test
```

## Credits

- This project includes FM samples in its automated tests by [Wohlstand](https://github.com/Wohlstand/libOPNMIDI/commits?author=Wohlstand).
