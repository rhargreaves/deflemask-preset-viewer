from ..preset import Preset


class Wopn():
    def __init__(self):
        self.magic_number = None
        self.version = None
        self.m_banks = None
        self.p_banks = None
        self.lfo_enable = None
        self.lfo_freq = None

    def generate_line(self, char):
        LINE_WIDTH = 60
        return (char * LINE_WIDTH) + '\n'

    def info(self):
        text = 'WOPN\n'
        text = text + 'M_Banks' + "{0:>5}\n".format(len(self.m_banks))
        text = text + 'P_Banks' + "{0:>5}\n".format(len(self.p_banks))
        text = text + 'LFO' + \
            "{0:>9}\n".format('On' if self.lfo_enable else 'Off')
        text = text + 'LFO Freq' + "{0:>4}\n".format(self.lfo_freq)
        for bank_index, bank in enumerate(self.m_banks):
            text = text + self.bank_info(bank, bank_index)
        return text

    def bank_info(self, bank, bank_index):
        text = self.generate_line('=')
        text = text + 'Bank' + \
            "{0:>8}".format(bank_index) + \
            '    ' + bank.name + '\n'
        text = text + self.generate_line('=')
        for instrument_index, instrument in enumerate(bank.instruments):
            text = text + self.instrument_info(instrument, instrument_index)
        return text

    def instrument_info(self, instrument, instrument_index):
        text = self.generate_line('-')
        text = text + 'Instrument' + \
            "{0:>5}".format(instrument_index) + \
            '    ' + instrument.name + '\n'
        text = text + self.generate_line('-')
        text = text + instrument.info()
        return text


class WopnInstrument(Preset):
    def __init__(self, name):
        Preset.__init__(self)
        self.name = name

    def info(self):
        return super(WopnInstrument, self).info()


class WopnBank():
    def __init__(self, name, index):
        self.name = name
        self.index = index
        self.instruments = []
