# Tai Sakuma <tai.sakuma@gmail.com>
import numpy as np

import pytest

from altdphi import AltDphi
from .testing import assert_altdphi_equal

from .expected import *

##__________________________________________________________________||
@pytest.fixture(
    params=[
        (event_nojet, altdphi_nojet, altdphi_met_nojet),
        (event_monojet, altdphi_monojet, altdphi_met_monojet),
        (event_two_jets, altdphi_two_jets, altdphi_met_two_jets),
        (event_three_jets, altdphi_three_jets, altdphi_met_three_jets),
        (event_four_jets, altdphi_four_jets, altdphi_met_four_jets),
        (event_twelve_jets, altdphi_twelve_jets, altdphi_met_twelve_jets),
    ],
    ids=('nojet', 'monojet', 'two_jets', 'three_jets', 'four_jets', 'twelve_jets')
)
def event_altdphi(request):
    return request.param

def test_altdphi(event_altdphi):
    event = event_altdphi[0]
    expected_altdphi = event_altdphi[1]
    pt = np.array(event['jet_pt'])
    phi = np.array(event['jet_phi'])
    actual_altdphi = AltDphi(pt=pt, phi=phi)
    assert_altdphi_equal(expected_altdphi, actual_altdphi)

def test_altdphi_met(event_altdphi):
    event = event_altdphi[0]
    expected_altdphi = event_altdphi[2]
    pt = np.array(event['jet_pt'])
    phi = np.array(event['jet_phi'])
    met = event['met']
    met_phi = event['met_phi']
    actual_altdphi = AltDphi(pt=pt, phi=phi, mht=met, mht_phi=met_phi)
    assert_altdphi_equal(expected_altdphi, actual_altdphi)

##__________________________________________________________________||
def test_altdphi_monojet_is_minus_mht():
    event = event_monojet
    pt = np.array(event['jet_pt'])
    phi = np.array(event['jet_phi'])
    altdphi = AltDphi(pt=pt, phi=phi)
    assert pt[0] == altdphi.mht
    assert [1] == altdphi.f
    assert [-1] == altdphi.cos_dphi

def test_altdphi_monojet_is_not_minus_mht():
    event = event_monojet
    pt = np.array(event['jet_pt'])
    phi = np.array(event['jet_phi'])
    mht = event['met']
    mht_phi = event['met_phi']
    altdphi = AltDphi(pt=pt, phi=phi, mht=mht, mht_phi=mht_phi)
    assert pt[0] != altdphi.mht
    assert [1] != altdphi.f
    assert [-1] != altdphi.cos_dphi

##__________________________________________________________________||
