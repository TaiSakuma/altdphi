# Tai Sakuma <tai.sakuma@gmail.com>
import numpy as np

import pytest

from .target import assert_equal
from altdphi import AltDphi

try:
    import unittest.mock as mock
except ImportError:
    import mock

##__________________________________________________________________||
def test_assert_equal_simple():

    pt = np.array([741.63,  498.69, 45.62])
    phi = np.array([-1.41,  1.81, 0.92])
    alt = AltDphi(pt=pt, phi=phi)

    target = mock.MagicMock(pt=pt, phi=phi, varnames=('pt', 'phi'))

    assert_equal(target, alt)

def test_assert_equal_raise_different_value():

    pt = np.array([741.63,  498.69, 45.62])
    phi = np.array([-1.41,  1.81, 0.92])
    alt = AltDphi(pt=pt, phi=phi)

    phi = np.array([-1.41,  1.81, 0.93])
    target = mock.MagicMock(pt=pt, phi=phi, varnames=('pt', 'phi'))

    with pytest.raises(AssertionError):
        assert_equal(target, alt)

def test_assert_equal_raise_nonexistent_var():

    pt = np.array([741.63,  498.69, 45.62])
    phi = np.array([-1.41,  1.81, 0.92])
    alt = AltDphi(pt=pt, phi=phi)

    eta = np.array([0.2,  0.1, -0.2])
    target = mock.MagicMock(pt=pt, phi=phi, eta=eta, varnames=('pt', 'phi', 'eta'))

    with pytest.raises(AssertionError):
        assert_equal(target, alt)

##__________________________________________________________________||
