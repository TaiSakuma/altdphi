# Tai Sakuma <tai.sakuma@cern.ch>
import numpy as np

from .altdphi import AltDphi

##__________________________________________________________________||
class jetDphiAttrs(object):
    def __init__(self, inJetPrefix, outJetPrefix, minJetPt = None):
        self.inJetPrefix = inJetPrefix
        self.outJetPrefix = outJetPrefix
        self.minJetPt = minJetPt

    def __repr__(self):
        name_value_pairs = (
            ('inJetPrefix', self.inJetPrefix),
            ('outJetPrefix', self.outJetPrefix),
            ('minJetPt', self.minJetPt),
        )
        return '{}({})'.format(
            self.__class__.__name__,
            ', '.join(['{} = {!r}'.format(n, v) for n, v in name_value_pairs]),
        )

    def begin(self, event):
        self.mht = [ ]
        self.pt = [ ]
        self.phi = [ ]
        self.dphi = [ ]
        self.dphiHat = [ ]
        self.dphiTilde = [ ]
        self.bDphi = [ ]
        self.omega = [ ]
        self.omegaHat = [ ]
        self.omegaTilde = [ ]
        self.chi = [ ]
        self.f = [ ]
        self.g = [ ]
        self.k = [ ]
        self.h = [ ]
        self.arccotF = [ ]
        self._attach_to_event(event)

    def _attach_to_event(self, event):
        setattr(event, 'mht_{}'.format(self.outJetPrefix), self.mht)
        setattr(event, '{}_pt'.format(self.outJetPrefix), self.pt)
        setattr(event, '{}_phi'.format(self.outJetPrefix), self.phi)
        setattr(event, '{}_dphi'.format(self.outJetPrefix), self.dphi)
        setattr(event, '{}_dphiHat'.format(self.outJetPrefix), self.dphiHat)
        setattr(event, '{}_dphiTilde'.format(self.outJetPrefix), self.dphiTilde)
        setattr(event, '{}_bDphi'.format(self.outJetPrefix), self.bDphi)
        setattr(event, '{}_omega'.format(self.outJetPrefix), self.omega)
        setattr(event, '{}_omegaHat'.format(self.outJetPrefix), self.omegaHat)
        setattr(event, '{}_omegaTilde'.format(self.outJetPrefix), self.omegaTilde)
        setattr(event, '{}_chi'.format(self.outJetPrefix), self.chi)
        setattr(event, '{}_f'.format(self.outJetPrefix), self.f)
        setattr(event, '{}_g'.format(self.outJetPrefix), self.g)
        setattr(event, '{}_k'.format(self.outJetPrefix), self.k)
        setattr(event, '{}_h'.format(self.outJetPrefix), self.h)
        setattr(event, '{}_arccotF'.format(self.outJetPrefix), self.arccotF)

    def event(self, event):
        self._attach_to_event(event)

        event_jet_pt = getattr(event, '{}_pt'.format(self.inJetPrefix))

        idxs = range(len(event_jet_pt))
        if self.minJetPt is not None:
            idxs = [i for i in idxs if event_jet_pt[i] >= self.minJetPt]

        self.pt[:] = [event_jet_pt[i] for i in idxs]

        event_jet_phi = getattr(event, '{}_phi'.format(self.inJetPrefix))
        self.phi[:] = [event_jet_phi[i] for i in idxs]

        pt = np.array(self.pt)
        phi = np.array(self.phi)

        alt = AltDphi(pt = pt, phi = phi)
        self.mht[:] = [alt.mht.item()]
        self.f[:] = alt.f
        self.arccotF[:] = alt.arccotF
        self.dphi[:] = alt.dphi
        self.dphiHat[:] = alt.dphiHat
        self.omega[:] = alt.omega
        self.omegaHat[:] = alt.omegaHat
        self.bDphi[:] = alt.bDphi
        self.g[:] = alt.g
        self.dphiTilde[:] = alt.dphiTilde
        self.omegaTilde[:] = alt.omegaTilde
        self.k[:] = alt.k
        self.chi[:] = alt.chi
        self.h[:] = alt.h

##__________________________________________________________________||
