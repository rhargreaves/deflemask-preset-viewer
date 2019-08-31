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

    assert wopn.lfo_enable == True
    assert wopn.lfo_freq == 1


def test_parses_melodic_bank_names():
    wopn = parse_wopn(SAMPLE_WOPN)

    assert wopn.m_banks[0].name == 'Standard :3'
    assert wopn.m_banks[1].name == 'XG SFX #000'


def test_parses_percussion_banks():
    wopn = parse_wopn(SAMPLE_WOPN)

    assert wopn.p_banks[0].name == 'XG #001 StandKit'
    assert wopn.p_banks[1].name == 'XG #049 SymphKit'


def test_there_are_128_instruments_in_melodic_banks():
    wopn = parse_wopn(SAMPLE_WOPN)

    for bank in wopn.m_banks:
        assert len(bank.instruments) == 128


def test_there_are_128_instruments_in_percussion_banks():
    wopn = parse_wopn(SAMPLE_WOPN)

    for bank in wopn.p_banks:
        assert len(bank.instruments) == 128


def test_parses_instruments_in_melodic_banks():
    wopn = parse_wopn(SAMPLE_WOPN)

    assert wopn.m_banks[0].instruments[0].name == '* GrandPiano'
    assert wopn.m_banks[0].instruments[1].name == '* BrightPiano'
    assert wopn.m_banks[1].instruments[0].name == ''


def test_parses_instrument_fm_parameters():
    wopn = parse_wopn(SAMPLE_WOPN)
    instrument = wopn.m_banks[0].instruments[0]

    assert instrument.algorithm == 2
    assert instrument.feedback == 0
    assert instrument.lfo_ams == 0
    assert instrument.lfo_fms == 0


def test_parses_instruments_in_percussion_banks():
    wopn = parse_wopn(SAMPLE_WOPN)

    assert wopn.p_banks[0].instruments[0].name == ''
    assert wopn.p_banks[0].instruments[1].name == ''
    assert wopn.p_banks[1].instruments[0].name == ''
