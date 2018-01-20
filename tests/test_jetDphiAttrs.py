# Tai Sakuma <tai.sakuma@gmail.com>
import pytest

try:
    import unittest.mock as mock
except ImportError:
    import mock

##__________________________________________________________________||
def test_with_sample(tbl_scan_event, tbl_scan_jet, scribblers):
    event = mock.MagicMock()
    event.jet_pt = [ ]
    event.jet_phi = [ ]

    for scribbler in scribblers:
        scribbler.begin(event)

    varnames = (
        'minbDphi', 'minOmega', 'minOmegaHat', 'minOmegaTilde',
        'minChi',
        # 'xi',
        'maxF'
    )

    for iloc in range(len(tbl_scan_event.index)):
        tbl_event = tbl_scan_event.iloc[iloc:(iloc + 1)]
        evt = tbl_event.evt.tolist()[0]
        tbl_jet = tbl_scan_jet[tbl_scan_jet.evt == evt]
        event.jet_pt[:] = tbl_jet.jet_pt.tolist()
        event.jet_phi[:] = tbl_jet.jet_phi.tolist()
        for scribbler in scribblers:
            scribbler.event(event)

        for varname in varnames:
            expected = tbl_event[varname].tolist()[0]
            actual = getattr(event, varname)[0]
            assert pytest.approx(expected, abs = 1e-6) == actual

##__________________________________________________________________||
def test_no_jet(scribblers):
    event = mock.MagicMock()
    event.jet_pt = [ ]
    event.jet_phi = [ ]

    for scribbler in scribblers:
        scribbler.begin(event)

    event.jet_pt[:] = [ ]
    event.jet_phi[:] = [ ]

    for scribbler in scribblers:
        scribbler.event(event)

    assert [0.0] == event.mht_jet40
    assert [ ] == event.jet40_pt
    assert [ ] == event.jet40_phi
    assert [ ] == event.jet40_dphi
    assert [ ] == event.jet40_dphiHat
    assert [ ] == event.jet40_dphiTilde
    assert [ ] == event.jet40_bDphi
    assert [ ] == event.jet40_omega
    assert [ ] == event.jet40_omegaHat
    assert [ ] == event.jet40_omegaTilde
    assert [ ] == event.jet40_chi
    assert [ ] == event.jet40_f
    assert [ ] == event.jet40_g
    assert [ ] == event.jet40_k
    assert [ ] == event.jet40_h
    assert [ ] == event.jet40_arccotF

    assert [-1] == event.minbDphi
    assert [-1] == event.minOmega
    assert [-1] == event.minOmegaHat
    assert [-1] == event.minOmegaTilde
    assert [-1] == event.minChi
    ## assert [-1] == event.xi
    assert [-1] == event.maxF

##__________________________________________________________________||
