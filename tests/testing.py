# Tai Sakuma <tai.sakuma@gmail.com>
import numpy as np

import pytest

##__________________________________________________________________||
def assert_altdphi_equal(expected, actual):
    for varname in expected.varnames:
        var_exp = getattr(expected, varname)

        try:
            var_act = getattr(actual, varname)
        except AttributeError as e:
            e.args = ("\nassert expected.{} == actual.{}\n{}".format(
                varname, varname, str(e)),
            )
            raise AssertionError(e)

        try:
            _assert_value_equal(var_exp, var_act)
        except AssertionError as e:
            e.args = ("\nassert expected.{} == actual.{}\n{!r} == {!r}\n{}".format(
                varname, varname, var_exp, var_act, str(e)),
            )
            raise AssertionError(e)

def _assert_value_equal(expected, actual):
    if _is_ndarray(expected):
        _assert_value_equal_ndarray(expected, actual)
        return

    if _is_scalar_nan(expected):
        _assert_value_equal_nan(expected, actual)
        return

    _assert_value_equal_else(expected, actual)

def _is_ndarray(v):
    return isinstance(v, np.ndarray)

def _assert_value_equal_ndarray(expected, actual):
    if not _is_ndarray(actual):
        raise AssertionError
    np.testing.assert_allclose(actual, expected, rtol=1e-5)

def _is_scalar_nan(v):
    if isinstance(v, float) and np.isnan(v):
        return True
    return False

def _assert_value_equal_nan(expected, actual):
    if not _is_scalar_nan(actual):
        raise AssertionError

def _assert_value_equal_else(expected, actual):
    assert pytest.approx(expected, rel=1e-7) == actual
    to_be_exact = (0.0, 1.0, -1.0, np.pi, np.pi/2, np.pi/4)
    if expected not in to_be_exact:
        return
    assert expected == actual

##__________________________________________________________________||
