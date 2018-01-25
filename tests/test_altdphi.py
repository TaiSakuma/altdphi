# Tai Sakuma <tai.sakuma@gmail.com>
import numpy as np

import pytest

from altdphi import AltDphi
from .testing import assert_altdphi_equal

from .expected import *

##__________________________________________________________________||
@pytest.mark.parametrize(
    'jets, expected', [
        pytest.param(nojet, altdphi_nojet, id='nojet'),
        pytest.param(monojet, altdphi_monojet, id='monojet'),
        pytest.param(two_jets, altdphi_two_jets, id='two_jets'),
        pytest.param(three_jets, altdphi_three_jets, id='three_jets'),
        pytest.param(four_jets, altdphi_four_jets, id='four_jets'),
    ]
)
def test_altdphi(jets, expected):
    pt = np.array(jets['pt'])
    phi = np.array(jets['phi'])
    actual = AltDphi(pt=pt, phi=phi)

    assert_altdphi_equal(expected, actual)

##__________________________________________________________________||
