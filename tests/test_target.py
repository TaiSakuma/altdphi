# Tai Sakuma <tai.sakuma@gmail.com>
import numpy as np

import pytest

from .target import TargetAltDphi
from altdphi import AltDphi

##__________________________________________________________________||
def test_simple():

    pt = np.array([741.63,  498.69, 45.62])
    phi = np.array([-1.41,  1.81, 0.92])
    alt = AltDphi(pt=pt, phi=phi)

    target = TargetAltDphi(pt=pt, phi=phi)

    target.assert_equal(alt)

def test_raise():

    pt = np.array([741.63,  498.69, 45.62])
    phi = np.array([-1.41,  1.81, 0.92])
    alt = AltDphi(pt=pt, phi=phi)

    phi = np.array([-1.41,  1.81, 0.93])
    target = TargetAltDphi(pt=pt, phi=phi)

    with pytest.raises(AssertionError):
        target.assert_equal(alt)

##__________________________________________________________________||
