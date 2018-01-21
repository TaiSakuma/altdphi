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
