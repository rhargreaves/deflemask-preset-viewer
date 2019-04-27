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


def op_values(name, values):
    return '{}\t{}\t{}\t{}\t{}\n'.format(
        name,
        values[0],
        values[1],
        values[2],
        values[3])


def test_returns_fm_parameters():
    for f in ["tests/sample_new.dmp", "tests/sample.dmp"]:
        stdout = subprocess.check_output(
            ["python3", "src/main.py", f]).decode()

    assert 'LFO FMS 0x00' in stdout
    assert 'Feedback 0x00' in stdout
    assert 'Algorithm 0x03' in stdout
    assert 'LFO AMS 0x00' in stdout
    assert op_values('Operator', [1, 2, 3, 4]) in stdout
    assert 'MUL\t14\t1\t0\t0\n' in stdout
    assert 'TL\t39\t24\t24\t19\n' in stdout
    assert 'AR\t31\t31\t31\t31\n' in stdout
    assert 'DR\t15\t14\t9\t9\n' in stdout
    assert 'SL\t14\t14\t14\t14\n' in stdout
