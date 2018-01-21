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

    target = mock.MagicMock(pt=pt, phi=phi, contents=('pt', 'phi'))

    assert_equal(target, alt)

def test_assert_equal_raise():

    pt = np.array([741.63,  498.69, 45.62])
    phi = np.array([-1.41,  1.81, 0.92])
    alt = AltDphi(pt=pt, phi=phi)

    phi = np.array([-1.41,  1.81, 0.93])
    target = mock.MagicMock(pt=pt, phi=phi, contents=('pt', 'phi'))

    with pytest.raises(AssertionError):
        assert_equal(target, alt)

##__________________________________________________________________||
