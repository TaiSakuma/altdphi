# Tai Sakuma <tai.sakuma@gmail.com>
import numpy as np

import pytest

try:
    import unittest.mock as mock
except ImportError:
    import mock

from altdphi import AltDphi
from .testing import assert_altdphi_equal

##__________________________________________________________________||
def test_with_sample(tbl_scan_event, tbl_scan_jet):

    for evt in tbl_scan_event.index:
        tbl_event = tbl_scan_event.loc[evt]
        tbl_jet = tbl_scan_jet.loc[[evt]]
        pt = tbl_jet.jet_pt.values
        phi = tbl_jet.jet_phi.values
        alt = AltDphi(pt=pt, phi=phi)

        expected = mock.MagicMock(
            min_dphi_star=tbl_event.minbDphi,
            min_omega=tbl_event.minOmega,
            min_omega_hat=tbl_event.minOmegaHat,
            min_omega_tilde=tbl_event.minOmegaTilde,
            min_chi=tbl_event.minChi,
            xi=tbl_event.xi,
            max_f=tbl_event.maxF
        )

        expected.varnames = (
            'min_dphi_star',
            'min_omega_hat',
            'min_omega_tilde',
            'min_chi',
            'xi',
            'max_f'
        )

        assert_altdphi_equal(expected, alt)

##__________________________________________________________________||
