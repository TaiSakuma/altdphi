# Tai Sakuma <tai.sakuma@gmail.com>
from __future__ import print_function
import numpy as np

import pytest

from altdphi import AltDphi

##__________________________________________________________________||
def test_repr_without_mht():
    pt =  np.array([1149.60, 794.66, 251.60, 94.48])
    phi = np.array([-1.32, 2.75, 0.87, -2.77])
    alt = AltDphi(pt=pt, phi=phi)

    # e.g.,
    # 'AltDphi(pt=array([ 741.63,  498.69,   45.62]), phi=array([-1.41,  1.81,  0.92]))'
    assert 'pt' in repr(alt)
    assert 'phi' in repr(alt)
    assert 'mht' not in repr(alt)
    assert 'mht_phi' not in repr(alt)

    assert repr(alt) + ':' == str(alt).split('\n')[0]
    assert repr(alt) + ':' == alt.to_string(all = True).split('\n')[0]

def test_repr_with_mht():
    pt =  np.array([1149.60, 794.66, 251.60, 94.48])
    phi = np.array([-1.32, 2.75, 0.87, -2.77])
    met = 783.54
    met_phi = 1.019
    alt = AltDphi(pt=pt, phi=phi, mht=met, mht_phi=met_phi)

    # e.g.,
    # 'AltDphi(pt=array([ 741.63,  498.69,   45.62]), phi=array([-1.41,  1.81,  0.92]), mht=264.16, mht_phi=1.44)'
    assert 'pt' in repr(alt)
    assert 'phi' in repr(alt)
    assert 'mht' in repr(alt)
    assert 'mht_phi' in repr(alt)

    assert repr(alt) + ':' == str(alt).split('\n')[0]
    assert repr(alt) + ':' == alt.to_string(all = True).split('\n')[0]

##__________________________________________________________________||
