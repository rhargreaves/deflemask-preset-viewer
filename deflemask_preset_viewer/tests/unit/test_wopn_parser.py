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
    instrument = wopn.m_banks[0].instruments[88]
    another_instrument = wopn.m_banks[0].instruments[4]

    assert instrument.algorithm == 4
    assert instrument.feedback == 1
    assert instrument.lfo_ams == 0
    assert instrument.lfo_fms == 0
    assert instrument.operators[0].mul == 7
    assert instrument.operators[0].dt == 0
    assert instrument.operators[0].tl == 25
    assert instrument.operators[0].rs == 0
    assert instrument.operators[0].ar == 15
    assert instrument.operators[0].am == 0
    assert instrument.operators[0].dr == 11
    assert instrument.operators[0].d2r == 6
    assert instrument.operators[0].sl == 7
    assert instrument.operators[0].rr == 6
    assert instrument.operators[0].ssg == 0
    assert instrument.operators[1].mul == 1
    assert instrument.operators[2].mul == 8
    assert instrument.operators[3].mul == 1
    assert another_instrument.operators[0].dt == 4
    assert another_instrument.operators[0].rs == 1


def test_parses_lfo_ams_instrument_fm_parameters():
    wopn = parse_wopn(SAMPLE_WOPN)
    instrument = wopn.m_banks[0].instruments[41]

    assert instrument.lfo_ams == 2
    assert instrument.lfo_fms == 3


def test_parses_instruments_in_percussion_banks():
    wopn = parse_wopn(SAMPLE_WOPN)

    assert wopn.p_banks[0].instruments[0].name == ''
    assert wopn.p_banks[0].instruments[1].name == ''
    assert wopn.p_banks[1].instruments[0].name == ''
