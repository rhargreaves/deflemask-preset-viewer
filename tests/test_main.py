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
    assert 'Algorithm 0x00' in stdout
