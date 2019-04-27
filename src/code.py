def print_code(dmp):
    print(
        "static const Channel SAMPLE = {{ {alg}, {fb}, {stereo}, {ams}, {fms}, {octave}, {freq} }}".format(
            alg=dmp.algorithm,
            fb=dmp.feedback,
            stereo=3,
            ams=dmp.lfo_ams,
            fms=dmp.lfo_fms,
            octave=0,
            freq=0
        ))
