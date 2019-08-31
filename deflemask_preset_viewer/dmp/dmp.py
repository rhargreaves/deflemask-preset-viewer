from ..preset import Preset


class Dmp(Preset):
    def __init__(self):
        Preset.__init__(self)
        self.version = None
        self.system_type = None
        self.instrument_mode = None

    def print_info(self):
        self.print_type()
        if self.instrument_mode == 1:
            print("Algorithm  {}       LFO FMS  {}".format(
                self.algorithm, self.lfo_fms))
            print("Feedback   {}       LFO AMS  {}".format(
                self.feedback, self.lfo_ams))
            self.print_operator_headers()
            self.print_op("MUL", lambda op: op.mul, self.operators)
            self.print_op("TL", lambda op: op.tl, self.operators)
            self.print_op("AR", lambda op: op.ar, self.operators)
            self.print_op("DR", lambda op: op.dr, self.operators)
            self.print_op("SL", lambda op: op.sl, self.operators)
            self.print_op("RR", lambda op: op.rr, self.operators)
            self.print_op("AM", lambda op: op.am, self.operators)
            self.print_op("RS", lambda op: op.rs, self.operators)
            self.print_op("DT", lambda op: op.dt, self.operators)
            self.print_op("D2R", lambda op: op.d2r, self.operators)
            self.print_op("SSG", lambda op: op.ssg, self.operators)

    def print_op(self, name, value_func, operators):
        print("{0:<11}".format(name), end='')
        for op in operators:
            print("{0:<8}".format(value_func(op)), end='')
        print()

    def print_operator_headers(self):
        print("Operator   ", end='')
        for i in range(4):
            print("{0:<8}".format(i+1), end='')
        print()

    def format_instrument_mode(self, mode):
        return "FM" if mode == 1 else "STD"

    def format_system(self, system_type):
        return "Genesis" if system_type == 2 else "Unknown"

    def print_type(self):
        print("{0:<11}{1:<8}{2:<9}{3:<7}".format(
            "Version",
            self.version,
            self.format_instrument_mode(self.instrument_mode),
            self.format_system(self.system_type)))
