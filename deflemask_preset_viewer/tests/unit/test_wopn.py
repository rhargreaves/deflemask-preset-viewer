from ...wopn.wopn import Wopn, WopnBank
import pytest


def test_returns_text_info():
    wopn = Wopn()
    wopn.lfo_enable = True
    wopn.lfo_freq = 1
    wopn.m_banks = [WopnBank('bank0', 0), WopnBank('bank1', 1)]
    wopn.p_banks = [WopnBank('bank0', 0), WopnBank(
        'bank1', 1), WopnBank('bank2', 2)]

    info = wopn.info()

    assert 'WOPN' in info
    assert 'M_Banks    2' in info
    assert 'P_Banks    3' in info
    assert 'LFO       On' in info
    assert 'LFO Freq   1' in info


@pytest.mark.skip(reason="WIP")
def test_returns_text_info_on_preset():
    wopn = Wopn()
    assert 'Algorithm' in wopn.info()
