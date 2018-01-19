# Tai Sakuma <tai.sakuma@gmail.com>
import pytest

try:
    import unittest.mock as mock
except ImportError:
    import mock

##__________________________________________________________________||
def test_one(tbl_scan_event, tbl_scan_jet, scribblers):
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
