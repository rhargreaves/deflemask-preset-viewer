import os


def const_name(filename):
    return os.path.splitext(os.path.basename(filename))[0].upper().replace(' ', '_')


def print_code(preset):
    STEREO_L_R = 3

    code = "static const Channel {name} = {{ {alg}, {fb}, {stereo}, {ams}, {fms}, {octave}, {freq}, {{ ".format(
        alg=preset.algorithm,
        fb=preset.feedback,
        stereo=STEREO_L_R,
        ams=preset.lfo_ams,
        fms=preset.lfo_fms,
        octave=0,
        freq=0,
        name=const_name(preset.name)
    )
    for i, op in enumerate(preset.operators):
        opDef = "{{ {mul}, {detune}, {ar}, {rs}, {dr}, {am}, {sa}, {d2r}, {rr}, {tl}, {ssg} }}".format(
            mul=op.mul,
            detune=op.dt,
            ar=op.ar,
            rs=op.rs,
            dr=op.dr,
            am=op.am,
            sa=op.sl,
            d2r=op.d2r,
            rr=op.rr,
            tl=op.tl,
            ssg=op.ssg)
        code += opDef
        if i != 3:
            code += ", "
    code += " } };"
    print(code)
