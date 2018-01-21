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
    ret.varnames = (
        'pt', 'phi', 'px', 'py',
        'mhtx', 'mhty', 'mht',
        'cos_dphi', 'sin_dphi', 'dphi',
        'f', 'arccot_f',
        'dphi_star',
        'sin_dphi_tilde', 'dphi_tilde', 'g',
        'omega', 'omega_tilde',
        'sin_dphi_hat', 'dphi_hat', 'omega_hat',
        'k', 'chi',
        'h',
        'min_omega_tilde', 'min_omega_hat', 'min_chi',
        'min_dphi_star',
        'min_omega',
        'min_dphi_tilde', 'min_sin_dphi_tilde',
        'max_f', 'max_h',
        'xi',
    )
    return ret

def test_nojet(expected_altdphi_nojet):
    pt = np.array([ ])
    phi = np.array([ ])
    actual = AltDphi(pt = pt, phi = phi)
    assert_altdphi_equal(expected_altdphi_nojet, actual)

##__________________________________________________________________||
def test_monojet():
    pt = np.array([1514.21328255])
    phi = np.array([-1.04235720634])
    alt = AltDphi(pt = pt, phi = phi)
    assert [1514.21328255] == alt.mht
    assert [1514.21328255] == alt.pt
    assert [-1.04235720634] == alt.phi
    assert [1] == alt.f
    assert [-1] == alt.cos_dphi
    assert [np.pi] == alt.dphi
    assert [np.pi/2] == alt.dphi_hat
    assert [np.pi] == alt.dphi_tilde
    assert [np.pi/2] == alt.dphi_star
    assert [0] == alt.omega
    assert [np.pi/4] == alt.omega_hat
    assert [0] == alt.omega_tilde
    assert [np.pi/2] == alt.chi
    assert [0] == alt.g
    assert [0] == alt.k
    assert [0] == alt.h
    assert [np.pi/4] == alt.arccot_f
    assert np.pi/2 == alt.min_dphi_star
    assert 0 == alt.min_omega
    assert np.pi/4 == alt.min_omega_hat
    assert 0 == alt.min_omega_tilde
    assert np.pi/2 == alt.min_chi
    assert np.pi/2 == alt.xi
    assert 1 == alt.max_f

##__________________________________________________________________||
