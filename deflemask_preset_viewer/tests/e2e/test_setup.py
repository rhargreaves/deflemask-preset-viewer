import subprocess


def test_package_installs_and_runs():
    stdout = subprocess.check_output(
        ["make", "install"]).decode()

    assert 'Successfully installed deflemask-preset-viewer' in stdout

    stdout = subprocess.check_output(
        ["deflemask-preset-viewer", "-h"]).decode()

    assert 'usage:' in stdout
