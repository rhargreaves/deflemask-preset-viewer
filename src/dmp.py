from .preset import Preset


class Dmp(Preset):
    def __init__(self):
        Preset.__init__(self)
        self.version = None
        self.system_type = None
        self.instrument_mode = None
