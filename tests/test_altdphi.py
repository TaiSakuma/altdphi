# Tai Sakuma <tai.sakuma@gmail.com>
import numpy as np

import pytest

from altdphi import AltDphi
from .testing import assert_altdphi_equal

from .expected import *

##__________________________________________________________________||
@pytest.fixture(
    params=[
        (event_nojet, altdphi_nojet),
        (event_monojet, altdphi_monojet),
        (event_two_jets, altdphi_two_jets),
        (event_three_jets, altdphi_three_jets),
        (event_four_jets, altdphi_four_jets),
    ],
    ids=('nojet', 'monojet', 'two_jets', 'three_jets', 'four_jets')
)
def event_altdphi(request):
    return request.param

def test_altdphi(event_altdphi):
    event, expected_altdphi = event_altdphi
    pt = np.array(event['jet_pt'])
    phi = np.array(event['jet_phi'])
    actual_altdphi = AltDphi(pt=pt, phi=phi)

    assert_altdphi_equal(expected_altdphi, actual_altdphi)

##__________________________________________________________________||
