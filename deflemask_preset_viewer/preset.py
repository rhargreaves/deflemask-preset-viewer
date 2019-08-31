from .ui import generate_line


class Preset:
    def __init__(self):
        self.name = None
        self.lfo_fms = None
        self.lfo_ams = None
        self.feedback = None
        self.algorithm = None
        self.operators = []

    def op(self, name, value_func, operators):
        header = "{0:<11}".format(name)
        optext = ''
        for op in operators:
            optext = optext + "{0:<8}".format(value_func(op))
        return header + optext + "\n"

    def operator_headers(self):
        text = generate_line('-')
        text = text + "Parameter  "
        for i in range(4):
            text = text + "Op {0:<5}".format(i + 1)
        text = text + '\n'
        generate_line('-')
        text = text + generate_line('-')
        return text

    def info(self):
        text = "Algorithm  {}       LFO FMS  {}\nFeedback   {}       LFO AMS  {}\n".format(
            self.algorithm, self.lfo_fms,
            self.feedback, self.lfo_ams)
        text = text + self.operator_headers()
        text = text + self.op("MUL", lambda op: op.mul, self.operators)
        text = text + self.op("TL", lambda op: op.tl, self.operators)
        text = text + self.op("AR", lambda op: op.ar, self.operators)
        text = text + self.op("D1R", lambda op: op.dr, self.operators)
        text = text + self.op("D1L", lambda op: op.sl, self.operators)
        text = text + self.op("RR", lambda op: op.rr, self.operators)
        text = text + self.op("AM", lambda op: op.am, self.operators)
        text = text + self.op("RS", lambda op: op.rs, self.operators)
        text = text + self.op("DT1", lambda op: op.dt, self.operators)
        text = text + self.op("D2R", lambda op: op.d2r, self.operators)
        text = text + self.op("SSG", lambda op: op.ssg, self.operators)
        return text
