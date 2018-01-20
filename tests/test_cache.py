# Tai Sakuma <tai.sakuma@gmail.com>
from altdphi.cache import cache_once_property

##__________________________________________________________________||
class Spam(object):
    def __init__(self, v):
        self.v = v
        self.n_eggs_called = 0

    @cache_once_property
    def eggs(self):
        self.n_eggs_called += 1
        return 2*self.v

##__________________________________________________________________||
def test_cache_once_property():
    s = Spam(10)
    assert 20 == s.eggs
    assert 20 == s.eggs
    assert 1 == s.n_eggs_called

    s = Spam(12)
    assert 24 == s.eggs
    assert 24 == s.eggs
    assert 1 == s.n_eggs_called

##__________________________________________________________________||
