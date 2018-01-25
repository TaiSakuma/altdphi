# Tai Sakuma <tai.sakuma@gmail.com>
import numpy as np

##__________________________________________________________________||
def dump_altdphi(altdphi, target_class='mock.MagicMock'):
    ret = '{}('.format(target_class)
    contests = [ ]
    for n in altdphi.varnames:
        v = getattr(altdphi, n)
        if isinstance(v, np.ndarray):
            l = '{}=np.array(['.format(n)
            l = l + ', '.join(('{!r}'.format(e) for e in v))
            l = l + '])'
        elif np.isnan(v):
            l = '{}=np.nan'.format(n, v)
        else:
            l = '{}=np.float64({})'.format(n, v)
        contests.append(l)
    contests.append('varnames=({})'.format(', '.join(("'{}'".format(n) for n in altdphi.varnames))))
    if contests:
        ret = ret + '\n    '
        ret = ret + ',\n    '.join(contests)
        ret = ret + '\n'
    ret = ret + ')'
    return ret

##__________________________________________________________________||
