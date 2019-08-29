from src.wopn_parser import parse_wopn


def test_reads_correct_magic_number():
    wopn = parse_wopn('tests/sample.wopn')

    assert wopn.magic_number == 'WOPN2-B2NK'


def test_reads_correct_version():
    wopn = parse_wopn('tests/sample.wopn')

    assert wopn.version == 2
