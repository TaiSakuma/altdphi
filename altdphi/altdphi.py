# Tai Sakuma <tai.sakuma@gmail.com>
import numpy as np

from cache import cache_once_property

##__________________________________________________________________||
class AltDphi(object):
    def __init__(self, pt, phi):
        self.pt = pt
        self.phi = phi

    def __repr__(self):
        name_value_pairs = (
            ('pt', self.pt),
            ('phi', self.phi),
        )
        return '{}({})'.format(
            self.__class__.__name__,
            ', '.join(['{} = {!r}'.format(n, v) for n, v in name_value_pairs]),
        )

    @cache_once_property
    def minbDphi(self):
        if self.bDphi.size == 0:
            return np.nan
        return self.bDphi.min()

    @cache_once_property
    def minOmega(self):
        if self.omega.size == 0:
            return np.nan
        return self.omega.min()

    @cache_once_property
    def minOmegaHat(self):
        if self.omegaHat.size == 0:
            return np.nan
        return self.omegaHat.min()

    @cache_once_property
    def minOmegaTilde(self):
        if self.omegaTilde.size == 0:
            return np.nan
        return self.omegaTilde.min()

    @cache_once_property
    def minChi(self):
        if self.chi.size == 0:
            return np.nan
        return self.chi.min()

    @cache_once_property
    def minDphiTilde(self):
        if self.dphiTilde.size == 0:
            return np.nan
        return self.dphiTilde.min()

    @cache_once_property
    def maxF(self):
        if self.f.size == 0:
            return np.nan
        return self.f.max()

    @cache_once_property
    def maxH(self):
        if self.h.size == 0:
            return np.nan
        return self.h.max()

    @cache_once_property
    def xi(self):
        if np.isnan(self.minDphiTilde):
            return np.nan
        sinMinDphiTilde = np.sin(self.minDphiTilde)
        return np.arctan2(sinMinDphiTilde, self.maxH)

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
        if self.pt.size == 1:
            ## this makes mht and pt precisely the same
            ## for the monojet events and prevent k from
            ## slightly deviating from zero, which, in turn,
            ## makes chi pi/2 for the monojet events
            return self.pt[0]

        return np.sqrt(self.mhtx**2 + self.mhty**2)

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
        return np.sqrt(1 - self.cosDphi**2)

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
        ret = np.where(
            (self.f == 1) & (self.cosDphi == -1),
            np.pi/2,
            np.arctan2(self.sinDphi, self.f + self.cosDphi)
        )
        return ret

    @cache_once_property
    def g(self):
        return np.maximum(self.cosDphi + self.f, 0)

    @cache_once_property
    def sinDphiTilde(self):
        return np.sqrt(1 + (self.g - self.f)**2 - 2*(self.g - self.f)*self.cosDphi)

    @cache_once_property
    def dphiTilde(self):
        return np.where(
            self.f + self.cosDphi >= 0,
            self.dphi,
            np.pi - np.arcsin(self.sinDphiTilde)
        )

    @cache_once_property
    def omegaTilde(self):
        return np.arctan2(self.sinDphiTilde, self.f)

    @cache_once_property
    def k(self):
        return np.minimum(self.f, self.g)

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
        if self.sinDphiTilde.size == 0:
            return np.array([ ])
        return np.where(self.sinDphiTilde == self.sinDphiTilde.min(), self.f + self.g, self.f)

##__________________________________________________________________||
