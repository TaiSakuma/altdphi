# Tai Sakuma <tai.sakuma@gmail.com>
import numpy as np

import pytest

try:
    import unittest.mock as mock
except ImportError:
    import mock

from altdphi import AltDphi
from .testing import assert_altdphi_equal

##__________________________________________________________________||
def test_with_sample(tbl_scan_event, tbl_scan_jet):

    for evt in tbl_scan_event.index:
        tbl_event = tbl_scan_event.loc[evt]
        tbl_jet = tbl_scan_jet.loc[[evt]]
        pt = tbl_jet.jet_pt.values
        phi = tbl_jet.jet_phi.values
        alt = AltDphi(pt = pt, phi = phi)

        expected = mock.MagicMock(
            min_dphi_star = tbl_event.minbDphi,
            min_omega = tbl_event.minOmega,
            min_omega_hat = tbl_event.minOmegaHat,
            min_omega_tilde = tbl_event.minOmegaTilde,
            min_chi = tbl_event.minChi,
            xi = tbl_event.xi,
            max_f = tbl_event.maxF
        )

        expected.varnames = (
            'min_dphi_star',
            'min_omega_hat',
            'min_omega_tilde',
            'min_chi',
            'xi',
            'max_f'
        )

        assert_altdphi_equal(expected, alt)

##__________________________________________________________________||
@pytest.fixture()
def expected_altdphi_nojet():
    ret = mock.MagicMock(
        pt = np.array([ ]),
        phi = np.array([ ]),
        px = np.array([ ]),
        py = np.array([ ]),
        mhtx = 0.0,
        mhty = 0.0,
        mht = 0.0,
        cos_dphi = np.array([ ]),
        sin_dphi = np.array([ ]),
        dphi = np.array([ ]),
        f = np.array([ ]),
        arccot_f = np.array([ ]),
        dphi_star = np.array([ ]),
        sin_dphi_tilde = np.array([ ]),
        dphi_tilde = np.array([ ]),
        g = np.array([ ]),
        omega = np.array([ ]),
        omega_tilde = np.array([ ]),
        sin_dphi_hat = np.array([ ]),
        dphi_hat = np.array([ ]),
        omega_hat = np.array([ ]),
        k = np.array([ ]),
        chi = np.array([ ]),
        h = np.array([ ]),
        min_omega_tilde = np.nan,
        min_omega_hat = np.nan,
        min_chi = np.nan,
        min_dphi_star = np.nan,
        min_omega = np.nan,
        min_dphi_tilde = np.nan,
        min_sin_dphi_tilde = np.nan,
        max_f = np.nan,
        max_h = np.nan,
        xi = np.nan,
    )
    ret.varnames = AltDphi.varnames
    return ret

def test_nojet(expected_altdphi_nojet):
    pt = np.array([ ])
    phi = np.array([ ])
    actual = AltDphi(pt = pt, phi = phi)
    assert_altdphi_equal(expected_altdphi_nojet, actual)

##__________________________________________________________________||
@pytest.fixture()
def expected_altdphi_monojet():
    ret = mock.MagicMock(
        cos_dphi = np.array([-1.0]),
        sin_dphi = np.array([0.0]),
        dphi = np.array([np.pi]),
        f = np.array([1.0]),
        arccot_f = np.array([np.pi/4]),
        dphi_star = np.array([np.pi/2]),
        sin_dphi_tilde = np.array([0.0]),
        dphi_tilde = np.array([np.pi]),
        g = np.array([0.0]),
        omega = np.array([0.0]),
        omega_tilde = np.array([0.0]),
        sin_dphi_hat = np.array([1.0]),
        dphi_hat = np.array([np.pi/2]),
        omega_hat = np.array([np.pi/4]),
        k = np.array([0.0]),
        chi = np.array([np.pi/2]),
        h = np.array([0.0]),
        min_omega_tilde = 0.0,
        min_omega_hat = np.pi/4,
        min_chi = np.pi/2,
        min_dphi_star = np.pi/2,
        min_omega = 0.0,
        min_dphi_tilde = np.pi,
        min_sin_dphi_tilde = 0.0,
        max_f = 1.0,
        max_h = 0.0,
        xi = np.pi/2,
    )
    varnames_not_totest = ('pt', 'phi', 'px', 'py', 'mhtx', 'mhty', 'mht')
    ret.varnames = [n for n in AltDphi.varnames if n not in varnames_not_totest]
    return ret

def test_monojet(expected_altdphi_monojet):
    pt = np.array([1514.21328255])
    phi = np.array([-1.04235720634])
    actual = AltDphi(pt = pt, phi = phi)
    assert_altdphi_equal(expected_altdphi_monojet, actual)

##__________________________________________________________________||
