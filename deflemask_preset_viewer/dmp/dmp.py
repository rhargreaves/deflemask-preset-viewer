from ..preset import Preset


class Dmp(Preset):
    def __init__(self):
        Preset.__init__(self)
        self.version = None
        self.system_type = None
        self.instrument_mode = None

    def info(self):
        text = self.dmp_type() + '\n'
        if self.instrument_mode == 1:
            text = text + "Algorithm  {}       LFO FMS  {}\nFeedback   {}       LFO AMS  {}\n".format(
                self.algorithm, self.lfo_fms,
                self.feedback, self.lfo_ams)
        text = text + self.operator_headers()
        text = text + self.op("MUL", lambda op: op.mul, self.operators)
        text = text + self.op("TL", lambda op: op.tl, self.operators)
        text = text + self.op("AR", lambda op: op.ar, self.operators)
        text = text + self.op("DR", lambda op: op.dr, self.operators)
        text = text + self.op("SL", lambda op: op.sl, self.operators)
        text = text + self.op("RR", lambda op: op.rr, self.operators)
        text = text + self.op("AM", lambda op: op.am, self.operators)
        text = text + self.op("RS", lambda op: op.rs, self.operators)
        text = text + self.op("DT", lambda op: op.dt, self.operators)
        text = text + self.op("D2R", lambda op: op.d2r, self.operators)
        text = text + self.op("SSG", lambda op: op.ssg, self.operators)
        return text

    def op(self, name, value_func, operators):
        header = "{0:<11}".format(name)
        optext = ''
        for op in operators:
            optext = optext + "{0:<8}".format(value_func(op))
        return header + optext + "\n"

    def operator_headers(self):
        text = "Operator   "
        for i in range(4):
            text = text + "{0:<8}".format(i+1)
        return text + '\n'

    def format_instrument_mode(self, mode):
        return "FM" if mode == 1 else "STD"

    def format_system(self, system_type):
        return "Genesis" if system_type == 2 else "Unknown"

    def dmp_type(self):
        return "{0:<11}{1:<8}{2:<9}{3:<7}".format(
            "Version",
            self.version,
            self.format_instrument_mode(self.instrument_mode),
            self.format_system(self.system_type))
