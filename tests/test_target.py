# Tai Sakuma <tai.sakuma@gmail.com>
import numpy as np

import pytest

from .target import TargetAltDphi
from altdphi import AltDphi

try:
    import unittest.mock as mock
except ImportError:
    import mock

##__________________________________________________________________||
def test_attributes():
    pt = mock.MagicMock()
    phi = mock.MagicMock()
    target = TargetAltDphi(pt=pt, phi=phi)
    assert pt is target.pt
    assert phi is target.phi

def test_attributes_raise():
    pt = mock.MagicMock()
    phi = mock.MagicMock()
    target = TargetAltDphi(pt=pt, phi=phi)
    with pytest.raises(AttributeError):
        target.eta

##__________________________________________________________________||
def test_assert_equal_simple():

    pt = np.array([741.63,  498.69, 45.62])
    phi = np.array([-1.41,  1.81, 0.92])
    alt = AltDphi(pt=pt, phi=phi)

    target = TargetAltDphi(pt=pt, phi=phi)

    target.assert_equal(alt)

def test_assert_equal_raise():

    pt = np.array([741.63,  498.69, 45.62])
    phi = np.array([-1.41,  1.81, 0.92])
    alt = AltDphi(pt=pt, phi=phi)

    phi = np.array([-1.41,  1.81, 0.93])
    target = TargetAltDphi(pt=pt, phi=phi)

    with pytest.raises(AssertionError):
        target.assert_equal(alt)

##__________________________________________________________________||
