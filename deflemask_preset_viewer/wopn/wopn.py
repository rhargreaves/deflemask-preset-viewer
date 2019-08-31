from ..preset import Preset


class Wopn(Preset):
    def __init__(self):
        Preset.__init__(self)
        self.magic_number = None
        self.version = None

    def print_info(self):
        print("WOPN")
