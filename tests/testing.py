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
    if isinstance(expected, np.ndarray):
        _assert_value_equal_ndarray(expected, actual)
        return

    _assert_value_equal_else(expected, actual)

def _assert_value_equal_else(expected, actual):
    assert pytest.approx(expected, abs = 1e-6) == actual
    to_be_exact = (0.0, 1.0, -1.0, np.pi, np.pi/2, np.pi/4)
    if expected not in to_be_exact:
        return
    assert expected == actual

def _assert_value_equal_ndarray(expected, actual):
    np.testing.assert_equal(expected, actual)

##__________________________________________________________________||
