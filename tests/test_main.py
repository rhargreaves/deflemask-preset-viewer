import subprocess


def test_returns_non_zero():
    subprocess.check_call(["python3", "src/main.py", "-h"])


def test_returns_details_for_version_8_dmp():
    stdout = subprocess.check_output(
        ["python3", "src/main.py", "tests/sample.dmp"]).decode()

    assert 'FM' in stdout
    assert 'Version 8' in stdout


def test_returns_details_for_version_11_dmp():
    stdout = subprocess.check_output(
        ["python3", "src/main.py", "tests/sample_new.dmp"]).decode()

    assert 'FM' in stdout
    assert 'Genesis' in stdout
    assert 'Version 11' in stdout


def test_returns_fm_parameters():
    for f in ["tests/sample_new.dmp", "tests/sample.dmp"]:
        stdout = subprocess.check_output(
            ["python3", "src/main.py", f]).decode()

    assert 'LFO FMS 0x00' in stdout
    assert 'Feedback 0x00' in stdout
    assert 'Algorithm 0x03' in stdout
    assert 'LFO AMS 0x00' in stdout
    assert op_values('Operator', [1, 2, 3, 4]) in stdout
    assert op_values('MUL', [14, 1, 0, 0]) in stdout
    assert op_values('TL', [39, 24, 24, 19]) in stdout
    assert op_values('AR', [31, 31, 31, 31]) in stdout
    assert op_values('DR', [15, 14, 9, 9]) in stdout
    assert op_values('SL', [14, 14, 14, 14]) in stdout
    assert op_values('RR', [15, 15, 15, 15]) in stdout


def op_values(name, values):
    return '{}\t{}\t{}\t{}\t{}\n'.format(
        name,
        values[0],
        values[1],
        values[2],
        values[3])
