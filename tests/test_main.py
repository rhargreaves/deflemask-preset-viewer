import subprocess


def test_returns_non_zero():
    subprocess.check_call(["python3", "src/main.py"])
