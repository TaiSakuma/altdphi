# Tai Sakuma <tai.sakuma@gmail.com>
import numpy as np

##__________________________________________________________________||
class AltDphi(object):
    def __init__(self, pt, phi):
        self.pt = pt
        self.phi = phi

    def f(self):
        px = self.pt*np.cos(self.phi)
        py = self.pt*np.sin(self.phi)

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
