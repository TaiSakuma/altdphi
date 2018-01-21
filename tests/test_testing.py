# Tai Sakuma <tai.sakuma@gmail.com>
import numpy as np

import pytest

from . import testing
from altdphi import AltDphi

try:
    import unittest.mock as mock
except ImportError:
    import mock

##__________________________________________________________________||
def test_assert_altdphi_equal_with_real_altdphi():

    pt = np.array([741.63,  498.69, 45.62])
    phi = np.array([-1.41,  1.81, 0.92])
    alt1 = AltDphi(pt=pt, phi=phi)

    pt = np.array([741.63,  498.69, 45.62])
    phi = np.array([-1.41,  1.81, 0.92])
    alt2 = AltDphi(pt=pt, phi=phi)

    testing.assert_altdphi_equal(alt1, alt2)

def test_assert_altdphi_equal_with_mock():

    pt = np.array([741.63,  498.69, 45.62])
    phi = np.array([-1.41,  1.81, 0.92])
    alt = AltDphi(pt=pt, phi=phi)

    target = mock.MagicMock(pt=pt, phi=phi)
    target.varnames = ('pt', 'phi')

    testing.assert_altdphi_equal(target, alt)

##__________________________________________________________________||
def test_assert_altdphi_equal_raise_different_value():

    pt = np.array([741.63,  498.69, 45.62])
    phi = np.array([-1.41,  1.81, 0.92])
    alt = AltDphi(pt=pt, phi=phi)

    phi = np.array([-1.41,  1.81, 0.93])
    target = mock.MagicMock(pt=pt, phi=phi, varnames=('pt', 'phi'))

    with pytest.raises(AssertionError):
        testing.assert_altdphi_equal(target, alt)

def test_assert_altdphi_equal_raise_nonexistent_var():

    pt = np.array([741.63,  498.69, 45.62])
    phi = np.array([-1.41,  1.81, 0.92])
    alt = AltDphi(pt=pt, phi=phi)

    eta = np.array([0.2,  0.1, -0.2])
    target = mock.MagicMock(pt=pt, phi=phi, eta=eta, varnames=('pt', 'phi', 'eta'))

    with pytest.raises(AssertionError):
        testing.assert_altdphi_equal(target, alt)

##__________________________________________________________________||
@pytest.mark.parametrize(
    'v1, v2', [
        pytest.param(np.float64(0.0045), np.float64(0.0045)+1e-7, id='general'),
        pytest.param(np.float64(0.0), np.float64(0.0), id='zero'),
        pytest.param(np.float64(1.0), np.float64(1.0), id='one'),
        pytest.param(np.float64(-1.0), np.float64(-1.0), id='minus_one'),
        pytest.param(np.pi, np.pi, id='pi'),
        pytest.param(np.pi/2, np.pi/2, id='pi_over_two'),
        pytest.param(np.pi/4, np.pi/4, id='pi_over_four'),
    ]
)
def test_assert_value_equal_else_approx_pass(v1, v2):
    testing._assert_value_equal_else(v1, v2)

@pytest.mark.parametrize(
    'v1, v2', [
        pytest.param(np.float64(0.0045), np.float64(0.0045)+1e-6, id='general'),
        pytest.param(np.float64(0.0), np.float64(0.0)+1e-15, id='zero'),
        pytest.param(np.float64(1.0), np.float64(1.0)+1e-15, id='one'),
        pytest.param(np.float64(-1.0), np.float64(-1.0)+1e-15, id='minus_one'),
        pytest.param(np.pi, np.pi+1e-15, id='pi'),
        pytest.param(np.pi/2, np.pi/2+1e-15, id='pi_over_two'),
        pytest.param(np.pi/4, np.pi/4+1e-15, id='pi_over_four'),
    ]
)
def test_assert_value_equal_else_approx_faile(v1, v2):
    with pytest.raises(AssertionError):
        testing._assert_value_equal_else(v1, v2)

##__________________________________________________________________||
@pytest.mark.parametrize(
    'v1, v2', [
        pytest.param(np.array([ ]), np.array([ ]), id='empty'),
    ]
)
def test_assert_value_equal_ndarray_pass(v1, v2):
    testing._assert_value_equal_ndarray(v1, v2)

@pytest.mark.parametrize(
    'v1, v2', [
        pytest.param(np.array([ ]), np.float64(0.0), id='np.float64'),
        pytest.param(np.array([ ]), np.nan, id='nan'),
    ]
)
def test_assert_value_equal_ndarray_fail(v1, v2):
    with pytest.raises(AssertionError):
        testing._assert_value_equal_ndarray(v1, v2)

##__________________________________________________________________||
