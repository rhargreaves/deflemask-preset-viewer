import os
import re
from .preset import Preset


def const_name(name):
    return re.sub("[^\\w\\s]", "", name).upper().replace(' ', '_').replace('__', '_')


def channel_code(preset):
    code = "{{ {alg}, {fb}, {ams}, {fms}, {{ ".format(
        alg=preset.algorithm,
        fb=preset.feedback,
        ams=preset.lfo_ams,
        fms=preset.lfo_fms,
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
    code += " } }"
    return code


def print_preset(preset, name):
    code = "static const FmPreset {} = {};".format(
        const_name(name), channel_code(preset))
    print(code)


def print_percussion_preset(preset, name):
    code = "static const PercussionPreset {} = {{ {}, {} }};".format(
        const_name(name), channel_code(preset), preset.percussion_key)
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
        name = preset_name(
            bank_index, instrument_index, instrument.name, prefix)
        if prefix == 'P':
            print_percussion_preset(instrument, name)
        else:
            print_preset(instrument, name)
        print('')
    print("const FmPreset* const {}_BANK_{}[] = {{".format(prefix, bank_index))
    for instrument_index, instrument in enumerate(bank.instruments):
        name = preset_name(
            bank_index, instrument_index, instrument.name, prefix)
        print("    &{}".format(const_name(name)), end='')
        print("" if instrument_index == 127 else ",")
    print("};\n")


def print_code(model):
    if isinstance(model, Preset):
        print_preset(model, model.name)
    else:
        print_wopn(model)
