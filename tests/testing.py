# Tai Sakuma <tai.sakuma@gmail.com>
import numpy as np

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
            e.args = ("\nassert expected.{} == actual.{}\n{}".format(
                varname, varname, str(e)),
            )
            raise AssertionError(e)

def _assert_value_equal(expected, actual):
    if isinstance(expected, np.ndarray):
        np.testing.assert_equal(expected, actual)
    else:
        assert expected == actual

##__________________________________________________________________||
