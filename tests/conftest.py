# Tai Sakuma <tai.sakuma@gmail.com>
import os
import pandas as pd
import numpy as np

import pytest

from altdphi.jetDphiAttrs import jetDphiAttrs
from altdphi.minimum import minimum
from altdphi.maximum import maximum
from altdphi.xi import xi

##__________________________________________________________________||
@pytest.fixture(scope = 'session')
def tbl_scan_event():
    tbl_path = os.path.join(os.path.dirname(__file__), 'data', 'tbl_scan_event.txt')
    ret =  pd.read_table(tbl_path, delim_whitespace = True, index_col = 'evt')

    ## fix for monojet events
    ret.loc[ret.njet == 1, 'minChi'] = np.pi/2.0
    return ret

@pytest.fixture(scope = 'session')
def tbl_scan_jet():
    tbl_path = os.path.join(os.path.dirname(__file__), 'data', 'tbl_scan_jet.txt')
    ret = pd.read_table(tbl_path, delim_whitespace = True, index_col = 'evt')
    return ret

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
