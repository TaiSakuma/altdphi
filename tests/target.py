# Tai Sakuma <tai.sakuma@gmail.com>
import numpy as np

##__________________________________________________________________||
class TargetAltDphi(object):
    def __init__(self, **contents):
        self.contents = contents

    def assert_equal(self, other):
        for varname in self.contents:
            target = self.contents[varname]
            actual = getattr(other, varname)
            try:
                self._assert_value_equal(target, actual)
            except AssertionError as e:
                e.args = ("\nassert target.{} == actual.{}{}".format(varname, varname, str(e)),)
                raise AssertionError(e)

    def _assert_value_equal(self, v1, v2):
        if isinstance(v1, np.ndarray):
            np.testing.assert_equal(v1, v2)
        else:
            assert v1 == v2

##__________________________________________________________________||
