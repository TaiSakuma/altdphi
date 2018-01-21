# Tai Sakuma <tai.sakuma@gmail.com>
import numpy as np

import pytest

from . import testing
from altdphi import AltDphi

try:
    import unittest.mock as mock
except ImportError:
    import mock

##__________________________________________________________________||
def test_assert_altdphi_equal_with_real_altdphi():

    pt = np.array([741.63,  498.69, 45.62])
    phi = np.array([-1.41,  1.81, 0.92])
    alt1 = AltDphi(pt=pt, phi=phi)

    pt = np.array([741.63,  498.69, 45.62])
    phi = np.array([-1.41,  1.81, 0.92])
    alt2 = AltDphi(pt=pt, phi=phi)

    testing.assert_altdphi_equal(alt1, alt2)

def test_assert_altdphi_equal_with_mock():

    pt = np.array([741.63,  498.69, 45.62])
    phi = np.array([-1.41,  1.81, 0.92])
    alt = AltDphi(pt=pt, phi=phi)

    target = mock.MagicMock(pt=pt, phi=phi)
    target.varnames = ('pt', 'phi')

    testing.assert_altdphi_equal(target, alt)

##__________________________________________________________________||
def test_assert_altdphi_equal_raise_different_value():

    pt = np.array([741.63,  498.69, 45.62])
    phi = np.array([-1.41,  1.81, 0.92])
    alt = AltDphi(pt=pt, phi=phi)

    phi = np.array([-1.41,  1.81, 0.93])
    target = mock.MagicMock(pt=pt, phi=phi, varnames=('pt', 'phi'))

    with pytest.raises(AssertionError):
        testing.assert_altdphi_equal(target, alt)

def test_assert_altdphi_equal_raise_nonexistent_var():

    pt = np.array([741.63,  498.69, 45.62])
    phi = np.array([-1.41,  1.81, 0.92])
    alt = AltDphi(pt=pt, phi=phi)

    eta = np.array([0.2,  0.1, -0.2])
    target = mock.MagicMock(pt=pt, phi=phi, eta=eta, varnames=('pt', 'phi', 'eta'))

    with pytest.raises(AssertionError):
        testing.assert_altdphi_equal(target, alt)

##__________________________________________________________________||
