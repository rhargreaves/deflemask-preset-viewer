from ..preset import Preset


class Wopn():
    def __init__(self):
        self.magic_number = None
        self.version = None

    def info(self):
        return 'WOPN'


class WponInstrument(Preset):
    pass


class WopnBank():
    def __init__(self, name, index):
        self.name = name
        self.index = index
        self.instruments = []
