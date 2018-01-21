# Tai Sakuma <tai.sakuma@gmail.com>
import numpy as np

import pytest

from altdphi.altdphi import AltDphi

##__________________________________________________________________||
def test_with_sample(tbl_scan_event, tbl_scan_jet):

    for evt in tbl_scan_event.index:
        tbl_event = tbl_scan_event.loc[evt]
        tbl_jet = tbl_scan_jet.loc[[evt]]
        pt = tbl_jet.jet_pt.values
        phi = tbl_jet.jet_phi.values
        alt = AltDphi(pt = pt, phi = phi)

        assert pytest.approx(tbl_event.minbDphi, abs = 1e-6) == alt.min_dphi_star
        assert pytest.approx(tbl_event.minOmega, abs = 1e-6) == alt.min_omega
        assert pytest.approx(tbl_event.minOmegaHat, abs = 1e-6) == alt.min_omega_hat
        assert pytest.approx(tbl_event.minOmegaTilde, abs = 1e-6) == alt.min_omega_tilde
        assert pytest.approx(tbl_event.minChi, abs = 1e-6) == alt.min_chi
        ## assert pytest.approx(tbl_event.xi, abs = 1e-6) == alt.xi
        assert pytest.approx(tbl_event.maxF, abs = 1e-6) == alt.max_f


def test_no_jet():
    pt = np.array([ ])
    phi = np.array([ ])
    alt = AltDphi(pt = pt, phi = phi)
    assert [0.0] == alt.mht
    assert [ ] == alt.pt.tolist()
    assert [ ] == alt.phi.tolist()
    assert [ ] == alt.dphi.tolist()
    assert [ ] == alt.dphi_hat.tolist()
    assert [ ] == alt.dphiTilde.tolist()
    assert [ ] == alt.dphi_star.tolist()
    assert [ ] == alt.omega.tolist()
    assert [ ] == alt.omega_hat.tolist()
    assert [ ] == alt.omegaTilde.tolist()
    assert [ ] == alt.chi.tolist()
    assert [ ] == alt.f.tolist()
    assert [ ] == alt.g.tolist()
    assert [ ] == alt.k.tolist()
    assert [ ] == alt.h.tolist()
    assert [ ] == alt.arccot_f.tolist()
    assert np.isnan(alt.min_dphi_star)
    assert np.isnan(alt.min_omega)
    assert np.isnan(alt.min_omega_hat)
    assert np.isnan(alt.min_omega_tilde)
    assert np.isnan(alt.min_chi)
    assert np.isnan(alt.xi)
    assert np.isnan(alt.max_f)

def test_monojet():
    pt = np.array([1514.21])
    phi = np.array([-1.042])
    alt = AltDphi(pt = pt, phi = phi)
    pt = np.array([151.21])
    assert [1514.21] == alt.mht
    assert [1514.21] == alt.pt
    assert [-1.042] == alt.phi
    assert [np.pi] == alt.dphi
    assert [np.pi/2] == alt.dphi_hat
    assert [np.pi] == alt.dphiTilde
    assert [np.pi/2] == alt.dphi_star
    assert [0] == alt.omega
    assert [np.pi/4] == alt.omega_hat
    assert [0] == alt.omegaTilde
    assert [np.pi/2] == alt.chi
    assert [1] == alt.f
    assert [0] == alt.g
    assert [0] == alt.k
    assert [1] == alt.h
    assert [np.pi/4] == alt.arccot_f
    assert np.pi/2 == alt.min_dphi_star
    assert 0 == alt.min_omega
    assert np.pi/4 == alt.min_omega_hat
    assert 0 == alt.min_omega_tilde
    assert np.pi/2 == alt.min_chi
    ## assert np.pi/2 == alt.xi
    assert 1 == alt.max_f

##__________________________________________________________________||
