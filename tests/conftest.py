# Tai Sakuma <tai.sakuma@gmail.com>
import os
import pandas as pd
import numpy as np

import pytest

##__________________________________________________________________||
@pytest.fixture(scope = 'session')
def tbl_scan_event():
    tbl_path = os.path.join(os.path.dirname(__file__), 'data', 'tbl_scan_event.txt')
    ret =  pd.read_table(tbl_path, delim_whitespace = True, index_col = 'evt')

    ## fix for monojet events
    ret.loc[ret.njet == 1, 'minChi'] = np.pi/2.0
    ret.loc[ret.njet == 1, 'xi'] = np.pi/2.0
    return ret

@pytest.fixture(scope = 'session')
def tbl_scan_jet():
    tbl_path = os.path.join(os.path.dirname(__file__), 'data', 'tbl_scan_jet.txt')
    ret = pd.read_table(tbl_path, delim_whitespace = True, index_col = 'evt')
    return ret

##__________________________________________________________________||
