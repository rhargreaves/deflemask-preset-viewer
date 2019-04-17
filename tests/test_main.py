import subprocess


def test_returns_non_zero():
    subprocess.check_call(["python3", "src/main.py", "-h"])


def test_returns_details_for_test_dmp():
    stdout = subprocess.check_output(
        ["python3", "src/main.py", "tests/sample.dmp"]).decode()

    assert 'FM' in stdout
