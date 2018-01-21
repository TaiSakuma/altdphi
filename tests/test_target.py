# Tai Sakuma <tai.sakuma@gmail.com>
import numpy as np

from .target import TargetAltDphi
from altdphi import AltDphi

##__________________________________________________________________||
def test_comp():

    pt = np.array([741.63,  498.69, 45.62])
    phi = np.array([-1.41,  1.81, 0.92])
    alt = AltDphi(pt=pt, phi=phi)
    alt = AltDphi(pt=pt, phi=phi)

    phi = np.array([-1.41,  1.81, 0.93])
    target = TargetAltDphi(pt=pt, phi=phi)

    target.assert_equal(alt)

##__________________________________________________________________||
