import os
import re
from .preset import Preset


def const_name(name):
    return re.sub("[^\w\s]", "", name).upper().replace(' ', '_').replace('__', '_')


def print_preset(preset, name):
    STEREO_L_R = 3

    code = "static const Channel {name} = {{ {alg}, {fb}, {stereo}, {ams}, {fms}, {octave}, {freq}, {{ ".format(
        alg=preset.algorithm,
        fb=preset.feedback,
        stereo=STEREO_L_R,
        ams=preset.lfo_ams,
        fms=preset.lfo_fms,
        octave=0,
        freq=0,
        name=const_name(name)
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


def preset_name(bank_index, instrument_index, name, prefix):
    if len(name) == 0:
        return "{}_BANK_{}_INST_{}".format(
            prefix, bank_index, instrument_index)
    else:
        return "{}_BANK_{}_INST_{}_{}".format(
            prefix, bank_index, instrument_index, name)


def print_wopn(wopn):
    for bank_index, bank in enumerate(wopn.m_banks):
        print_wopn_bank(bank, bank_index, 'M')
    for bank_index, bank in enumerate(wopn.p_banks):
        print_wopn_bank(bank, bank_index, 'P')


def print_wopn_bank(bank, bank_index, prefix):
    for instrument_index, instrument in enumerate(bank.instruments):
        print_preset(instrument, preset_name(
            bank_index, instrument_index, instrument.name, prefix))
        print('')
    print("const Channel* const {}_BANK_{}[] = {{".format(prefix, bank_index))
    for instrument_index, instrument in enumerate(bank.instruments):
        if instrument_index == 127:
            print("    &{}".format(const_name(preset_name(
                bank_index, instrument_index, instrument.name, prefix))))
        else:
            print("    &{},".format(const_name(preset_name(
                bank_index, instrument_index, instrument.name, prefix))))
    print("};\n")


def print_code(model):
    if isinstance(model, Preset):
        print_preset(model, model.name)
    else:
        print_wopn(model)
