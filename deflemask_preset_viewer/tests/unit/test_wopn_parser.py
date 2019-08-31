from ...wopn.wopn_parser import parse_wopn


def test_reads_correct_magic_number():
    wopn = parse_wopn('deflemask_preset_viewer/tests/data/sample.wopn')

    assert wopn.magic_number == 'WOPN2-B2NK'


def test_reads_correct_version():
    wopn = parse_wopn('deflemask_preset_viewer/tests/data/sample.wopn')

    assert wopn.version == 2


def test_parses_number_of_melodic_instruments():
    wopn = parse_wopn('deflemask_preset_viewer/tests/data/sample.wopn')

    assert wopn.m_bank_count == 2


def test_parses_number_of_percussion_instruments():
    wopn = parse_wopn('deflemask_preset_viewer/tests/data/sample.wopn')

    assert wopn.p_bank_count == 5


def test_parses_global_flags():
    wopn = parse_wopn('deflemask_preset_viewer/tests/data/sample.wopn')

    assert wopn.global_flags == 9


def test_parses_melodic_banks():
    wopn = parse_wopn('deflemask_preset_viewer/tests/data/sample.wopn')

    for bank in wopn.m_banks:
        assert bank.name != ''


def test_parses_percussion_banks():
    wopn = parse_wopn('deflemask_preset_viewer/tests/data/sample.wopn')

    for bank in wopn.p_banks:
        assert bank.name != ''
