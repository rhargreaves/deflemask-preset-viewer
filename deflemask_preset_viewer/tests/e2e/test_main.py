import subprocess
import pytest
from ..data.files import SAMPLE_WOPN, SAMPLE_DMP, SAMPLE_NEW_DMP


def test_returns_help_page():
    stdout = subprocess.check_output(
        ["python3", "-m", "deflemask_preset_viewer", "-h"]).decode()

    assert 'usage:' in stdout


def test_returns_details_for_wopn():
    stdout = subprocess.check_output(
        ["python3", "-m", "deflemask_preset_viewer",
         SAMPLE_WOPN]).decode()

    assert 'WOPN' in stdout
    assert 'M_Banks' in stdout
    assert 'P_Banks' in stdout


def test_returns_details_for_version_8_dmp():
    stdout = subprocess.check_output(
        ["python3", "-m", "deflemask_preset_viewer",
         SAMPLE_DMP]).decode()

    assert 'FM' in stdout
    assert 'Version    8' in stdout


def test_returns_details_for_version_11_dmp():
    stdout = subprocess.check_output(
        ["python3", "-m", "deflemask_preset_viewer",
         SAMPLE_NEW_DMP]).decode()

    assert 'FM' in stdout
    assert 'Genesis' in stdout
    assert 'Version    11' in stdout


def test_returns_fm_parameters():
    for f in [SAMPLE_NEW_DMP, SAMPLE_DMP]:
        stdout = subprocess.check_output(
            ["python3", "-m", "deflemask_preset_viewer", f]).decode()

    assert 'LFO FMS  0' in stdout
    assert 'Feedback   0' in stdout
    assert 'Algorithm  3' in stdout
    assert 'LFO AMS  0' in stdout
    assert op_values('MUL', [14, 1, 0, 0]) in stdout
    assert op_values('TL', [39, 24, 24, 19]) in stdout
    assert op_values('AR', [31, 31, 31, 31]) in stdout
    assert op_values('D1R', [15, 14, 9, 9]) in stdout
    assert op_values('D1L', [14, 14, 14, 14]) in stdout
    assert op_values('RR', [15, 15, 15, 15]) in stdout
    assert op_values('AM', [0, 0, 0, 0]) in stdout
    assert op_values('RS', [2, 0, 0, 0]) in stdout
    assert op_values('DT1', [3, 3, 3, 3]) in stdout
    assert op_values('D2R', [0, 0, 0, 0]) in stdout
    assert op_values('SSG', [0, 0, 0, 0]) in stdout


@pytest.mark.skip(reason="WIP")
def test_returns_fm_parameters_in_wopn():
    stdout = subprocess.check_output(
        ["python3", "-m", "deflemask_preset_viewer",
            SAMPLE_WOPN]).decode()

    assert 'LFO FMS  0' in stdout
    assert 'Feedback   0' in stdout
    assert 'Algorithm  3' in stdout
    assert 'LFO AMS  0' in stdout
    assert op_values('MUL', [14, 1, 0, 0]) in stdout
    assert op_values('TL', [39, 24, 24, 19]) in stdout
    assert op_values('AR', [31, 31, 31, 31]) in stdout
    assert op_values('DR', [15, 14, 9, 9]) in stdout
    assert op_values('SL', [14, 14, 14, 14]) in stdout
    assert op_values('RR', [15, 15, 15, 15]) in stdout
    assert op_values('AM', [0, 0, 0, 0]) in stdout
    assert op_values('RS', [2, 0, 0, 0]) in stdout
    assert op_values('DT', [3, 3, 3, 3]) in stdout
    assert op_values('D2R', [0, 0, 0, 0]) in stdout
    assert op_values('SSG', [0, 0, 0, 0]) in stdout


def op_values(name, values):
    return '{0:<11}{1:<8}{2:<8}{3:<8}{4:<8}\n'.format(
        name,
        values[0],
        values[1],
        values[2],
        values[3])


def test_outputs_in_midi_interface_code_format():
    stdout = subprocess.check_output(
        ["python3", "-m", "deflemask_preset_viewer",
         SAMPLE_DMP, "-c"]).decode()

    assert stdout == 'static const Channel SAMPLE = ' + \
        '{ 3, 0, 3, 0, 0, 0, 0, { ' + \
        '{ 14, 3, 31, 2, 15, 0, 14, 0, 15, 39, 0 }, ' + \
        '{ 1, 3, 31, 0, 14, 0, 14, 0, 15, 24, 0 }, ' + \
        '{ 0, 3, 31, 0, 9, 0, 14, 0, 15, 24, 0 }, ' + \
        '{ 0, 3, 31, 0, 9, 0, 14, 0, 15, 19, 0 } } };\n'


def test_outputs_wopn_instruments_in_midi_interface_code_format():
    stdout = subprocess.check_output(
        ["python3", "-m", "deflemask_preset_viewer",
         SAMPLE_WOPN, "-c"]).decode()

    assert 'static const Channel M_BANK_0_INST_0_GRANDPIANO = ' in stdout
    assert 'static const Channel M_BANK_0_INST_2_ELECTRICPIANO_ANIMATICS = ' in stdout
    assert 'static const Channel M_BANK_1_INST_126 = ' in stdout


def test_outputs_wopn_instrument_array_in_midi_interface_code_format():
    stdout = subprocess.check_output(
        ["python3", "-m", "deflemask_preset_viewer",
         SAMPLE_WOPN, "-c"]).decode()

    assert "const Channel* const M_BANK_0[] = {\n" + \
        "    &M_BANK_0_INST_0_GRANDPIANO,\n" + \
        "    &M_BANK_0_INST_1_BRIGHTPIANO,\n" + \
        "    &M_BANK_0_INST_2_ELECTRICPIANO_ANIMATICS,\n" in stdout
    assert "    &M_BANK_0_INST_127_GUNSHOT\n};\n" in stdout
