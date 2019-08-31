from ..preset import Preset


class Wopn():
    def __init__(self):
        self.magic_number = None
        self.version = None
        self.m_banks = None
        self.p_banks = None
        self.lfo_enable = None
        self.lfo_freq = None

    def info(self):
        text = 'WOPN\n'
        text = text + 'M_Banks' + "{0:>5}\n".format(len(self.m_banks))
        text = text + 'P_Banks' + "{0:>5}\n".format(len(self.p_banks))
        text = text + 'LFO' + \
            "{0:>9}\n".format('On' if self.lfo_enable else 'Off')
        text = text + 'LFO Freq' + "{0:>4}\n".format(self.lfo_freq)
        return text


class WponInstrument(Preset):
    pass


class WopnBank():
    def __init__(self, name, index):
        self.name = name
        self.index = index
        self.instruments = []
