# Tai Sakuma <tai.sakuma@gmail.com>
import numpy as np

from .cache import cache_once_property

##__________________________________________________________________||
class AltDphi(object):
    varnames = (
        'pt', 'phi', 'px', 'py',
        'mhtx', 'mhty', 'mht',
        'cos_dphi', 'sin_dphi', 'dphi',
        'f', 'arccot_f',
        'dphi_star',
        'sin_dphi_tilde', 'dphi_tilde', 'g',
        'omega', 'omega_tilde',
        'sin_dphi_hat', 'dphi_hat', 'omega_hat',
        'k', 'chi',
        'h',
        'min_omega_tilde', 'min_omega_hat', 'min_chi',
        'min_dphi_star',
        'min_omega',
        'min_dphi_tilde', 'min_sin_dphi_tilde',
        'max_f', 'max_h',
        'xi',
    )

    def __init__(self, pt, phi, mht=None, mht_phi=None):
        self.pt = pt
        self.phi = phi

        self.monojet_is_minus_mht = mht is None and pt.size == 1

        if mht is not None:
            self.mht = mht
            self.mhtx = mht*np.cos(mht_phi)
            self.mhty = mht*np.sin(mht_phi)

    def __repr__(self):
        name_value_pairs = (
            ('pt', self.pt),
            ('phi', self.phi),
        )
        return '{}({})'.format(
            self.__class__.__name__,
            ', '.join(['{}={!r}'.format(n, v) for n, v in name_value_pairs]),
        )

    def __str__(self):
        len_varname = max(len(n) for n in self.varnames)
        ret = '{!r}:'.format(self) + '\n'
        ret = ret + '\n'.join(
            ['    {:>{}}: {}'.format(n, len_varname, str(getattr(self, n))) for n in self.varnames]
        )
        return ret

    ##______________________________________________________________||
    @cache_once_property
    def min_omega_tilde(self):
        if self.omega_tilde.size == 0:
            return np.nan
        return self.omega_tilde.min()

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
        if np.isnan(self.min_sin_dphi_tilde):
            return np.nan
        if self.monojet_is_minus_mht:
            return np.pi/2
        return np.arctan2(self.min_sin_dphi_tilde, self.max_h)

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
    def min_sin_dphi_tilde(self):
        if self.sin_dphi_tilde.size == 0:
            return np.nan
        return self.sin_dphi_tilde.min()

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
        if self.monojet_is_minus_mht:
            ## make mht and pt precisely the same for monojet
            return self.pt[0]
        return np.sqrt(self.mhtx**2 + self.mhty**2)

    ##______________________________________________________________||
    @cache_once_property
    def cos_dphi(self):
        if self.monojet_is_minus_mht:
            return np.array([-1.0])
        ret = (self.mhtx*self.px + self.mhty*self.py)/(self.mht*self.pt)
        ret = np.minimum(ret, 1.0)
        ret = np.maximum(ret, -1.0)
        return ret

    @cache_once_property
    def sin_dphi(self):
        return np.sqrt(1 - self.cos_dphi**2)

    @cache_once_property
    def dphi(self):
        return np.arccos(self.cos_dphi)

    @cache_once_property
    def f(self):
        return self.pt/self.mht

    @cache_once_property
    def arccot_f(self):
        return np.arctan2(1, self.f)

    ##______________________________________________________________||
    @cache_once_property
    def dphi_star(self):
        ret = np.where(
            (self.f == 1) & (self.cos_dphi == -1),
            np.pi/2,
            np.arctan2(self.sin_dphi, self.f + self.cos_dphi)
        )
        return ret

    ##______________________________________________________________||
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
    def g(self):
        return np.maximum(self.f + self.cos_dphi, 0)

    ##______________________________________________________________||
    @cache_once_property
    def omega(self):
        return np.arctan2(self.sin_dphi, self.f)

    ##______________________________________________________________||
    @cache_once_property
    def omega_tilde(self):
        return np.arctan2(self.sin_dphi_tilde, self.f)

    ##______________________________________________________________||
    @cache_once_property
    def dphi_hat(self):
        return np.minimum(self.dphi, np.pi/2.0)

    @cache_once_property
    def sin_dphi_hat(self):
        return np.sin(self.dphi_hat)

    @cache_once_property
    def omega_hat(self):
        return np.arctan2(self.sin_dphi_hat, self.f)

    ##______________________________________________________________||
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

    ##______________________________________________________________||
    @cache_once_property
    def h(self):
        if self.sin_dphi_tilde.size == 0:
            return np.array([ ])
        return np.where(
            self.sin_dphi_tilde == self.sin_dphi_tilde.min(),
            self.g, self.f
        )

##__________________________________________________________________||
