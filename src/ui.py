from .wopn import Wopn


def print_op(name, value_func, operators):
    print("{0:<11}".format(name), end='')
    for i in [0, 2, 1, 3]:
        op = operators[i]
        print("{0:<8}".format(value_func(op)), end='')
    print()


def print_operator_headers():
    print("Operator   ", end='')
    for i in range(4):
        print("{0:<8}".format(i+1), end='')
    print()


def format_instrument_mode(mode):
    return "FM" if mode == 1 else "STD"


def format_system(system_type):
    return "Genesis" if system_type == 2 else "Unknown"


def print_type(dmp):
    print("{0:<11}{1:<8}{2:<9}{3:<7}".format(
        "Version",
        dmp.version,
        format_instrument_mode(dmp.instrument_mode),
        format_system(dmp.system_type)))


def print_dmp(dmp):
    if isinstance(dmp, Wopn):
        print(dmp.info())
    else:
        print_type(dmp)
        if dmp.instrument_mode == 1:
            print("Algorithm  {}       LFO FMS  {}".format(
                dmp.algorithm, dmp.lfo_fms))
            print("Feedback   {}       LFO AMS  {}".format(
                dmp.feedback, dmp.lfo_ams))
            print_operator_headers()
            print_op("MUL", lambda op: op.mul, dmp.operators)
            print_op("TL", lambda op: op.tl, dmp.operators)
            print_op("AR", lambda op: op.ar, dmp.operators)
            print_op("DR", lambda op: op.dr, dmp.operators)
            print_op("SL", lambda op: op.sl, dmp.operators)
            print_op("RR", lambda op: op.rr, dmp.operators)
            print_op("AM", lambda op: op.am, dmp.operators)
            print_op("RS", lambda op: op.rs, dmp.operators)
            print_op("DT", lambda op: op.dt, dmp.operators)
            print_op("D2R", lambda op: op.d2r, dmp.operators)
            print_op("SSG", lambda op: op.ssg, dmp.operators)
