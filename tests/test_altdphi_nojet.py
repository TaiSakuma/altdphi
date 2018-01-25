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
def expected_altdphi_nojet():
    ret = mock.MagicMock(
        pt=np.array([ ]),
        phi=np.array([ ]),
        px=np.array([ ]),
        py=np.array([ ]),
        mhtx=0.0,
        mhty=0.0,
        mht=0.0,
        cos_dphi=np.array([ ]),
        sin_dphi=np.array([ ]),
        dphi=np.array([ ]),
        f=np.array([ ]),
        arccot_f=np.array([ ]),
        dphi_star=np.array([ ]),
        sin_dphi_tilde=np.array([ ]),
        dphi_tilde=np.array([ ]),
        g=np.array([ ]),
        omega=np.array([ ]),
        omega_tilde=np.array([ ]),
        sin_dphi_hat=np.array([ ]),
        dphi_hat=np.array([ ]),
        omega_hat=np.array([ ]),
        k=np.array([ ]),
        chi=np.array([ ]),
        h=np.array([ ]),
        min_omega_tilde=np.nan,
        min_omega_hat=np.nan,
        min_chi=np.nan,
        min_dphi_star=np.nan,
        min_omega=np.nan,
        min_dphi_tilde=np.nan,
        min_sin_dphi_tilde=np.nan,
        max_f=np.nan,
        max_h=np.nan,
        xi=np.nan,
    )
    ret.varnames = AltDphi.varnames
    return ret

def test_nojet(expected_altdphi_nojet):
    pt = np.array([ ])
    phi = np.array([ ])
    actual = AltDphi(pt=pt, phi=phi)
    assert_altdphi_equal(expected_altdphi_nojet, actual)

##__________________________________________________________________||
