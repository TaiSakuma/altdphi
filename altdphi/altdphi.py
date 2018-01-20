# Tai Sakuma <tai.sakuma@gmail.com>
import numpy as np

from cache import cache_once_property

##__________________________________________________________________||
class AltDphi(object):
    def __init__(self, pt, phi):
        self.pt = pt
        self.phi = phi

    @cache_once_property
    def px(self):
        px = self.pt*np.cos(self.phi)
        return px

    @cache_once_property
    def py(self):
        py = self.pt*np.sin(self.phi)
        return py

    @cache_once_property
    def f(self):
        px = self.px
        py = self.py

        # MHT
        mhtx = -np.sum(px)
        mhty = -np.sum(py)
        mht = np.sqrt(mhtx**2 + mhty**2)
        if self.pt.size == 1: mht = self.pt[0] ## this makes mht and pt precisely the same
                                     ## for the monojet events and prevent k from
                                     ## slightly deviating from zero, which, in turn,
                                     ## makes chi pi/2 for the monojet events

        # f
        f = self.pt/mht
        return f

##__________________________________________________________________||
