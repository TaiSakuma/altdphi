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
        return self.pt*np.cos(self.phi)

    @cache_once_property
    def py(self):
        return self.pt*np.sin(self.phi)

    @cache_once_property
    def mhtx(self):
        return -np.sum(self.px)

    @cache_once_property
    def mhty(self):
        return -np.sum(self.py)

    @cache_once_property
    def mht(self):
        mht = np.sqrt(self.mhtx**2 + self.mhty**2)

        if self.pt.size == 1:
            ## this makes mht and pt precisely the same
            ## for the monojet events and prevent k from
            ## slightly deviating from zero, which, in turn,
            ## makes chi pi/2 for the monojet events
            mht = self.pt[0]

        return mht

    @cache_once_property
    def f(self):
        return self.pt/self.mht

    @cache_once_property
    def arccotF(self):
        return np.arctan2(1, self.f)

    @cache_once_property
    def cosDphi(self):
        ret = (self.mhtx*self.px + self.mhty*self.py)/(self.mht*self.pt)
        ret = np.minimum(ret, 1.0)
        ret = np.maximum(ret, -1.0)
        return ret

    @cache_once_property
    def dphi(self):
        return np.arccos(self.cosDphi)

    @cache_once_property
    def sinDphi(self):
        return np.sin(self.dphi)

    @cache_once_property
    def dphiHat(self):
        return np.minimum(self.dphi, np.pi/2.0)

    @cache_once_property
    def sinDphiHat(self):
        return np.sin(self.dphiHat)

    @cache_once_property
    def omega(self):
        return np.arctan2(self.sinDphi, self.f)

    @cache_once_property
    def omegaHat(self):
        return np.arctan2(self.sinDphiHat, self.f)

    @cache_once_property
    def bDphi(self):
        sqfc = np.sqrt(1 + self.f**2 + 2*self.f*self.cosDphi)
        cosbDphi = (self.f + self.cosDphi)/np.where(sqfc == 0, 1, sqfc) ## cosbDphi is 0 when sqfc == 0
                                                              ## np.where is used to avoid dividing by 0

        cosbDphi = np.minimum(cosbDphi, 1.0)
        cosbDphi = np.maximum(cosbDphi, -1.0)

        return np.arccos(cosbDphi)

    @cache_once_property
    def g(self):
        # FIXME: with the definition of g in the paper <>
        return np.maximum(self.cosDphi, -self.f)

    @cache_once_property
    def sinDphiTilde(self):
        # should be the same as np.where(f + cosDphi >= 0, sinDphi, sinDphi/sinbDphi)
        return np.sqrt(1 + self.g**2 - 2*self.g*self.cosDphi)

    @cache_once_property
    def dphiTilde(self):
        # FIXME: with the definition in the paper <>
        return np.arcsin(self.sinDphiTilde)

    @cache_once_property
    def omegaTilde(self):
        return np.arctan2(self.sinDphiTilde, self.f)

    @cache_once_property
    def k(self):
        return np.minimum(self.f, self.f + self.g)

    @cache_once_property
    def chi(self):
        both_zero = np.where(self.sinDphiTilde == 0, np.where(self.k == 0, True, False), False)
        ret = np.where(
            both_zero,                            ## np.arctan2(0, 0) returns 0
            np.pi/2,                              ## but chi should be pi/2
            np.arctan2(self.sinDphiTilde, self.k) ## when both sinDphiTilde and k are 0
        )
        return ret

    @cache_once_property
    def h(self):
        return np.where(self.sinDphiTilde == self.sinDphiTilde.min(), self.f + self.g, self.f)

##__________________________________________________________________||
