# Tai Sakuma <tai.sakuma@gmail.com>
import numpy as np
import pytest

try:
    import unittest.mock as mock
except ImportError:
    import mock

from altdphi import AltDphi

from . import expected
from .testing import assert_altdphi_equal

from .dump import dump_altdphi, dump_float

##__________________________________________________________________||
@pytest.fixture(
    params=[
        expected.event_nojet, expected.event_monojet, expected.event_two_jets,
        expected.event_three_jets, expected.event_four_jets, expected.event_twelve_jets,
    ],
    ids=('nojet', 'monojet', 'two_jets', 'three_jets', 'four_jets', 'twelve_jets')
)
def event(request):
    return request.param

##__________________________________________________________________||
def test_dump_altdphi(event):
    pt = np.array(event['jet_pt'])
    phi = np.array(event['jet_phi'])
    altdphi = AltDphi(pt=pt, phi=phi)
    dumped_string = dump_altdphi(altdphi)
    restored_mock = eval(dumped_string)
    assert_altdphi_equal(altdphi, restored_mock)

##__________________________________________________________________||
dumped = (
    "int('1')",
    "float('1.0')",
    "float('0.058741')",
    "np.float64('0.058741202537691072')",
    "np.float64(np.pi)",
    "np.float64(np.pi/2)",
    "np.float64(np.pi/4)",
)

##__________________________________________________________________||
@pytest.mark.parametrize('dumped', dumped)
def test_dump_float(dumped):
    value = eval(dumped)
    assert dumped == dump_float(value)

##__________________________________________________________________||
