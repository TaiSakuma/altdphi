# Tai Sakuma <tai.sakuma@gmail.com>
import numpy as np

##__________________________________________________________________||
def dump_altdphi(altdphi, target_class='mock.MagicMock'):
    ret = '{}('.format(target_class)
    contents = [ ]
    for n in altdphi.varnames:
        v = getattr(altdphi, n)
        if isinstance(v, np.ndarray):
            l = '{}=np.array(['.format(n)
            l = l + ', '.join(('{!r}'.format(e) for e in v))
            l = l + '])'
        elif np.isnan(v):
            l = '{}=np.nan'.format(n)
        else:
            l = '{}=np.float64({!r})'.format(n, v)
        contents.append(l)
    contents.append('varnames=({})'.format(', '.join(("'{}'".format(n) for n in altdphi.varnames))))
    if contents:
        ret = ret + '\n    '
        ret = ret + ',\n    '.join(contents)
        ret = ret + '\n'
    ret = ret + ')'
    return ret

##__________________________________________________________________||
