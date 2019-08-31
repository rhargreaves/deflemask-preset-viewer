from ..preset import Preset


class Wopn():
    def __init__(self):
        self.magic_number = None
        self.version = None
        self.m_banks = None
        self.p_banks = None

    def info(self):
        text = 'WOPN\n'
        text = text + 'M_Banks' + "{0:>4}\n".format(len(self.m_banks))
        text = text + 'P_Banks' + "{0:>4}\n".format(len(self.p_banks))
        return text


class WponInstrument(Preset):
    pass


class WopnBank():
    def __init__(self, name, index):
        self.name = name
        self.index = index
        self.instruments = []
