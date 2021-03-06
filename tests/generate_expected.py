#!/usr/bin/env python
# Tai Sakuma <tai.sakuma@gmail.com>
from __future__ import print_function
import os, sys

import numpy as np

from conftest import tbl_scan_event as tbl_scan_event_
from conftest import tbl_scan_jet as tbl_scan_jet_

from dump import dump_altdphi, dump_float

here = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(1, os.path.dirname(here))
from altdphi import AltDphi

##__________________________________________________________________||
expected_py_head = """
# this file is generated by {}
import numpy as np

try:
    import unittest.mock as mock
except ImportError:
    import mock
""".format(os.path.basename(__file__))
expected_py_head = expected_py_head.lstrip()

##__________________________________________________________________||
def main():

    njet_name_dict = {
        0: 'nojet',
        1: 'monojet',
        2: 'two_jets',
        3: 'three_jets',
        4: 'four_jets',
       12: 'twelve_jets'
    }

    event_dict = collect_event_data(njet_name_dict)

    expected_as_string = compose_expected_as_string(event_dict, njet_name_dict)

    print(expected_py_head)
    print(expected_as_string)

def collect_event_data(njet_name_dict):

    tbl_scan_event = tbl_scan_event_()
    tbl_scan_jet = tbl_scan_jet_()

    njet_list = sorted(njet_name_dict.keys())

    event_dict = { }

    njet_list_ = list(njet_list)

    # nojet
    event_dict[0] = dict(pt=np.array([ ]), phi=np.array([ ]), met=10.12, met_phi=2.41)
    njet_list_.remove(0)

    # 1 or more jets
    for evt in tbl_scan_event.index:
        tbl_event = tbl_scan_event.loc[evt]
        tbl_jet = tbl_scan_jet.loc[[evt]]

        njet = int(tbl_event.njet)
        if njet not in njet_list_:
            continue

        pt = tbl_jet.jet_pt.values
        phi = tbl_jet.jet_phi.values
        met = tbl_event.met_pt
        met_phi = tbl_event.met_phi
        event_dict[njet] = dict(pt=pt, phi=phi, met=met, met_phi=met_phi)

        njet_list_.remove(njet)
        if not njet_list_:
            break

    return event_dict

def compose_expected_as_string(event_dict, njet_name_dict):

    njet_list = sorted(event_dict.keys())

    contents = [ ]
    for njet in njet_list:
        njet_name = njet_name_dict[njet]
        event = event_dict[njet]
        pt = event['pt']
        phi = event['phi']
        met = event['met']
        met_phi = event['met_phi']
        alt = AltDphi(pt=pt, phi=phi)
        dumped = dump_altdphi(alt)
        alt_met = AltDphi(pt=pt, phi=phi, mht=met, mht_phi=met_phi)
        dumped_met = dump_altdphi(alt_met)
        lines = ''
        lines = lines + 'event_{} = dict(\n'.format(njet_name)
        lines = lines + '    jet_pt =  np.array([' + ', '.join([dump_float(v) for v in pt]) + ']),\n'
        lines = lines + '    jet_phi = np.array([' + ', '.join([dump_float(v) for v in phi]) + ']),\n'
        lines = lines + '    met = {}'.format(dump_float(met)) + ',\n'
        lines = lines + '    met_phi = {}'.format(dump_float(met_phi)) + ',\n'
        lines = lines + ')\n'
        lines = lines + '\n'
        lines = lines + 'altdphi_{} = {}\n'.format(njet_name, dumped)
        lines = lines + '\n'
        lines = lines + 'altdphi_met_{} = {}\n'.format(njet_name, dumped_met)
        contents.append(lines)

    return '\n'.join(contents)

##__________________________________________________________________||
if __name__ == '__main__':
    main()
