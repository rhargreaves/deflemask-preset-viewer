from ...wopn.wopn import Wopn
import pytest


def test_returns_text_info():
    wopn = Wopn()
    assert wopn.info() == "WOPN"


@pytest.mark.skip(reason="WIP")
def test_returns_text_info_on_preset():
    wopn = Wopn()
    assert 'Algorithm' in wopn.info()
