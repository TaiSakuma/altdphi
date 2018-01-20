# Tai Sakuma <tai.sakuma@gmail.com>
import numpy as np

import pytest

from altdphi.altdphi import AltDphi

##__________________________________________________________________||
def test_with_sample(tbl_scan_event, tbl_scan_jet):

    for evt in tbl_scan_event.index:
        tbl_event = tbl_scan_event.loc[evt]
        tbl_jet = tbl_scan_jet.loc[[evt]]
        pt = tbl_jet.jet_pt.values
        phi = tbl_jet.jet_phi.values
        alt = AltDphi(pt = pt, phi = phi)

        assert pytest.approx(tbl_event.minbDphi, abs = 1e-6) == alt.minbDphi
        assert pytest.approx(tbl_event.minOmega, abs = 1e-6) == alt.minOmega
        assert pytest.approx(tbl_event.minOmegaHat, abs = 1e-6) == alt.minOmegaHat
        assert pytest.approx(tbl_event.minOmegaTilde, abs = 1e-6) == alt.minOmegaTilde
        assert pytest.approx(tbl_event.minChi, abs = 1e-6) == alt.minChi
        ## assert pytest.approx(tbl_event.xi, abs = 1e-6) == alt.xi
        assert pytest.approx(tbl_event.maxF, abs = 1e-6) == alt.maxF


def test_no_jet():
    pt = np.array([ ])
    phi = np.array([ ])
    alt = AltDphi(pt = pt, phi = phi)
    assert np.isnan(alt.minbDphi)
    assert np.isnan(alt.minOmega)
    assert np.isnan(alt.minOmegaHat)
    assert np.isnan(alt.minOmegaTilde)
    assert np.isnan(alt.minChi)
    assert np.isnan(alt.xi)
    assert np.isnan(alt.maxF)

def test_monojet():
    pt = np.array([1514.21])
    phi = np.array([-1.042])
    alt = AltDphi(pt = pt, phi = phi)
    assert np.pi/2 == alt.minbDphi
    assert 0 == alt.minOmega
    assert np.pi/4 == alt.minOmegaHat
    assert 0 == alt.minOmegaTilde
    assert np.pi/2 == alt.minChi
    ## assert np.pi/2 == alt.xi
    assert 1 == alt.maxF

##__________________________________________________________________||
