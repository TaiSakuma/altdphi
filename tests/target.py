# Tai Sakuma <tai.sakuma@gmail.com>
import numpy as np

##__________________________________________________________________||
def assert_equal(expected, actual):
    for varname in expected.contents:
        expected_var = getattr(expected, varname)
        actual_var = getattr(actual, varname)
        try:
            _assert_value_equal(expected_var, actual_var)
        except AssertionError as e:
            e.args = ("\nassert expected.{} == actual.{}{}".format(varname, varname, str(e)),)
            raise AssertionError(e)

def _assert_value_equal(expected, actual):
    if isinstance(expected, np.ndarray):
        np.testing.assert_equal(expected, actual)
    else:
        assert expected == actual

##__________________________________________________________________||
