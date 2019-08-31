from ...wopn.wopn import Wopn


def test_returns_text_info():
    wopn = Wopn()
    assert wopn.info() == "WOPN"
