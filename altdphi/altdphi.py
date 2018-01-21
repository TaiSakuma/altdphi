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

    ##______________________________________________________________||
    @cache_once_property
    def min_omega_tilde(self):
        if self.omegaTilde.size == 0:
            return np.nan
        return self.omegaTilde.min()

    @cache_once_property
    def min_omega_hat(self):
        if self.omega_hat.size == 0:
            return np.nan
        return self.omega_hat.min()

    @cache_once_property
    def min_chi(self):
        if self.chi.size == 0:
            return np.nan
        return self.chi.min()

    @cache_once_property
    def xi(self):
        if np.isnan(self.min_dphi_tilde):
            return np.nan
        sinMinDphiTilde = np.sin(self.min_dphi_tilde)
        return np.arctan2(sinMinDphiTilde, self.max_h)

    ##______________________________________________________________||
    @cache_once_property
    def min_dphi_star(self):
        if self.dphi_star.size == 0:
            return np.nan
        return self.dphi_star.min()

    @cache_once_property
    def min_omega(self):
        if self.omega.size == 0:
            return np.nan
        return self.omega.min()

    @cache_once_property
    def min_dphi_tilde(self):
        if self.dphi_tilde.size == 0:
            return np.nan
        return self.dphi_tilde.min()

    @cache_once_property
    def max_f(self):
        if self.f.size == 0:
            return np.nan
        return self.f.max()

    @cache_once_property
    def max_h(self):
        if self.h.size == 0:
            return np.nan
        return self.h.max()

    ##______________________________________________________________||
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

    ##______________________________________________________________||
    @cache_once_property
    def f(self):
        return self.pt/self.mht

    @cache_once_property
    def arccot_f(self):
        return np.arctan2(1, self.f)

    @cache_once_property
    def cos_dphi(self):
        ret = (self.mhtx*self.px + self.mhty*self.py)/(self.mht*self.pt)
        ret = np.minimum(ret, 1.0)
        ret = np.maximum(ret, -1.0)
        return ret

    @cache_once_property
    def dphi(self):
        return np.arccos(self.cos_dphi)

    @cache_once_property
    def sin_dphi(self):
        return np.sqrt(1 - self.cos_dphi**2)

    ##______________________________________________________________||
    @cache_once_property
    def dphi_hat(self):
        return np.minimum(self.dphi, np.pi/2.0)

    @cache_once_property
    def sin_dphi_hat(self):
        return np.sin(self.dphi_hat)

    @cache_once_property
    def omega(self):
        return np.arctan2(self.sin_dphi, self.f)

    @cache_once_property
    def omega_hat(self):
        return np.arctan2(self.sin_dphi_hat, self.f)

    @cache_once_property
    def dphi_star(self):
        ret = np.where(
            (self.f == 1) & (self.cos_dphi == -1),
            np.pi/2,
            np.arctan2(self.sin_dphi, self.f + self.cos_dphi)
        )
        return ret

    @cache_once_property
    def g(self):
        return np.maximum(self.f + self.cos_dphi, 0)

    @cache_once_property
    def sin_dphi_tilde(self):
        return np.sqrt(1 + (self.g - self.f)**2 - 2*(self.g - self.f)*self.cos_dphi)

    @cache_once_property
    def dphi_tilde(self):
        return np.where(
            self.f + self.cos_dphi >= 0,
            self.dphi,
            np.pi - np.arcsin(self.sin_dphi_tilde)
        )

    @cache_once_property
    def omegaTilde(self):
        return np.arctan2(self.sin_dphi_tilde, self.f)

    @cache_once_property
    def k(self):
        return np.minimum(self.f, self.g)

    @cache_once_property
    def chi(self):
        ret = np.where(
            (self.f == 1) & (self.cos_dphi == -1),
            np.pi/2,
            np.arctan2(self.sin_dphi_tilde, self.k)
        )
        return ret

    @cache_once_property
    def h(self):
        if self.sin_dphi_tilde.size == 0:
            return np.array([ ])
        return np.where(self.sin_dphi_tilde == self.sin_dphi_tilde.min(), self.f + self.g, self.f)

##__________________________________________________________________||
