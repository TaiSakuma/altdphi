# Tai Sakuma <tai.sakuma@gmail.com>
import os
import pandas as pd
import numpy as np

import pytest

try:
    import unittest.mock as mock
except ImportError:
    import mock

from altdphi.jetDphiAttrs import jetDphiAttrs
from altdphi.minimum import minimum
from altdphi.maximum import maximum
from altdphi.xi import xi

##__________________________________________________________________||
@pytest.fixture(scope = 'module')
def tbl_scan_event():
    tbl_path = os.path.join(os.path.dirname(__file__), 'data', 'tbl_scan_event.txt')
    ret =  pd.read_table(tbl_path, delim_whitespace = True)

    ## fix for monojet events
    ret.loc[ret.njet == 1, 'minChi'] = np.pi/2.0
    return ret

@pytest.fixture(scope = 'module')
def tbl_scan_jet():
    tbl_path = os.path.join(os.path.dirname(__file__), 'data', 'tbl_scan_jet.txt')
    return pd.read_table(tbl_path, delim_whitespace = True)

@pytest.fixture()
def scribblers():
    sequence = [
        jetDphiAttrs(inJetPrefix = 'jet', outJetPrefix = 'jet40', minJetPt = 40),
        minimum(srcName = 'jet40_dphi', outName = 'minDphi', default_value = -1),
        minimum(srcName = 'jet40_bDphi', outName = 'minbDphi', default_value = -1),
        minimum(srcName = 'jet40_dphiTilde', outName = 'minDphiTilde', default_value = -1),
        minimum(srcName = 'jet40_omega', outName = 'minOmega', default_value = -1),
        minimum(srcName = 'jet40_omegaHat', outName = 'minOmegaHat', default_value = -1),
        minimum(srcName = 'jet40_omegaTilde', outName = 'minOmegaTilde', default_value = -1),
        minimum(srcName = 'jet40_chi', outName = 'minChi', default_value = -1),
        minimum(srcName = 'jet40_arccotF', outName = 'minArccotF', default_value = -1),
        maximum(srcName = 'jet40_dphi', outName = 'maxDphi', default_value = -1),
        maximum(srcName = 'jet40_f', outName = 'maxF', default_value = -1),
        maximum(srcName = 'jet40_h', outName = 'maxH', default_value = -1),
        xi(srcMinDphiTilde = 'minDphiTilde', srcMaxH = 'maxH', outName = 'xi'),
    ]
    return sequence

##__________________________________________________________________||
def test_one(tbl_scan_event, tbl_scan_jet, scribblers):
    event = mock.MagicMock()
    event.jet_pt = [ ]
    event.jet_phi = [ ]

    for scribbler in scribblers:
        scribbler.begin(event)

    varnames = (
        'minbDphi', 'minOmega', 'minOmegaHat', 'minOmegaTilde',
        'minChi',
        # 'xi',
        'maxF'
    )

    for iloc in range(len(tbl_scan_event.index)):
        tbl_event = tbl_scan_event.iloc[iloc:(iloc + 1)]
        evt = tbl_event.evt.tolist()[0]
        tbl_jet = tbl_scan_jet[tbl_scan_jet.evt == evt]
        event.jet_pt[:] = tbl_jet.jet_pt.tolist()
        event.jet_phi[:] = tbl_jet.jet_phi.tolist()
        for scribbler in scribblers:
            scribbler.event(event)

        for varname in varnames:
            expected = tbl_event[varname].tolist()[0]
            actual = getattr(event, varname)[0]
            assert pytest.approx(expected, abs = 1e-6) == actual

##__________________________________________________________________||
