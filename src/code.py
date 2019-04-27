def print_code(dmp):
    code = "static const Channel SAMPLE = {{ {alg}, {fb}, {stereo}, {ams}, {fms}, {octave}, {freq}, ".format(
        alg=dmp.algorithm,
        fb=dmp.feedback,
        stereo=3,
        ams=dmp.lfo_ams,
        fms=dmp.lfo_fms,
        octave=0,
        freq=0
    )
    for i in [0, 2, 1, 3]:
        op = dmp.operators[i]
        opDef = "{{ {mul}, {detune}, {ar}, {rs}, {dr}, {am}, {sa}, {d2r}, {rr}, {tl} }}".format(
            mul=op.mul,
            detune=op.dt,
            ar=op.ar,
            rs=op.rs,
            dr=op.dr,
            am=op.am,
            sa=op.sl,
            d2r=op.d2r,
            rr=op.rr,
            tl=op.tl)
        code += opDef
        if i != 3:
            code += ", "
    code += " };"
    print(code)
