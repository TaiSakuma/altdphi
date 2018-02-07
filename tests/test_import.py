# Tai Sakuma <tai.sakuma@gmail.com>
import pytest

from altdphi.altdphi import *

##__________________________________________________________________||
def test_AltDphi():
    AltDphi

##__________________________________________________________________||
def test_nameerror_1():
    with pytest.raises(NameError):
        cache_once_property

def test_nameerror_2():
    with pytest.raises(NameError):
        np

##__________________________________________________________________||

