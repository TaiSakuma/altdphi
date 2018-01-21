# Tai Sakuma <tai.sakuma@gmail.com>
import numpy as np

##__________________________________________________________________||
class TargetAltDphi(object):
    def __init__(self, **contents):
        self.contents = contents

    def __getattr__(self, name):
        try:
            return self.contents[name]
        except KeyError:
            raise AttributeError("'{}' object has no attribute '{}'".format(self.__class__.__name__, name))

##__________________________________________________________________||
def assert_equal(self, other):
    for varname in self.contents:
        target = getattr(self, varname)
        actual = getattr(other, varname)
        try:
            _assert_value_equal(target, actual)
        except AssertionError as e:
            e.args = ("\nassert target.{} == actual.{}{}".format(varname, varname, str(e)),)
            raise AssertionError(e)

def _assert_value_equal(v1, v2):
    if isinstance(v1, np.ndarray):
        np.testing.assert_equal(v1, v2)
    else:
        assert v1 == v2

##__________________________________________________________________||
