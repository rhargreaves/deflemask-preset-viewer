from ...wopn.wopn import Wopn, WopnBank, WopnInstrument
import pytest

wopn = Wopn()


def setup_module(module):
    wopn.lfo_enable = True
    wopn.lfo_freq = 1
    wopn.m_banks = [WopnBank('bank0', 0), WopnBank('bank1', 1)]
    wopn.p_banks = [WopnBank('bank0', 0), WopnBank(
        'bank1', 1), WopnBank('bank2', 2)]
    wopn.m_banks[0].instruments = [WopnInstrument()]
    wopn.m_banks[1].instruments = [WopnInstrument()]
    wopn.p_banks[0].instruments = [WopnInstrument()]
    wopn.p_banks[1].instruments = [WopnInstrument()]
    wopn.p_banks[2].instruments = [WopnInstrument()]


def test_returns_wopn_version_info():
    info = wopn.info()

    assert 'WOPN' in info


def test_returns_bank_count_info():
    info = wopn.info()

    assert 'M_Banks    2' in info
    assert 'P_Banks    3' in info


def test_returns_global_lfo_info():
    info = wopn.info()

    assert 'LFO       On' in info
    assert 'LFO Freq   1' in info


def test_returns_text_info_on_preset():
    info = wopn.info()

    assert 'Algorithm' in info
