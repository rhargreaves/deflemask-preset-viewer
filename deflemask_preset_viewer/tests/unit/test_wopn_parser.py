from ...wopn.wopn_parser import parse_wopn
from ..data.files import SAMPLE_WOPN


def test_reads_correct_magic_number():
    wopn = parse_wopn(SAMPLE_WOPN)

    assert wopn.magic_number == 'WOPN2-B2NK'


def test_reads_correct_version():
    wopn = parse_wopn(SAMPLE_WOPN)

    assert wopn.version == 2


def test_parses_number_of_melodic_instruments():
    wopn = parse_wopn(SAMPLE_WOPN)

    assert wopn.m_bank_count == 2


def test_parses_number_of_percussion_instruments():
    wopn = parse_wopn(SAMPLE_WOPN)

    assert wopn.p_bank_count == 5


def test_parses_global_flags():
    wopn = parse_wopn(SAMPLE_WOPN)

    assert wopn.global_flags == 9


def test_parses_melodic_banks():
    wopn = parse_wopn(SAMPLE_WOPN)

    for bank in wopn.m_banks:
        assert bank.name != ''


def test_parses_percussion_banks():
    wopn = parse_wopn(SAMPLE_WOPN)

    for bank in wopn.p_banks:
        assert bank.name != ''


def test_parses_instruments_in_melodic_banks():
    wopn = parse_wopn(SAMPLE_WOPN)

    for bank in wopn.m_banks:
        assert len(bank.instruments) == 128
        for i, instrument in enumerate(bank.instruments):

            assert instrument.name != None, "name of instrument %r is None" % i
            assert instrument.algorithm != None, "algorithm of instument %r is None" % i


def test_parses_instruments_in_percussion_banks():
    wopn = parse_wopn(SAMPLE_WOPN)

    for bank in wopn.p_banks:
        assert len(bank.instruments) == 128
        for i, instrument in enumerate(bank.instruments):

            assert instrument.name != None, "name of instrument %r is None" % i
            assert instrument.algorithm != None, "algorithm of instument %r is None" % i
