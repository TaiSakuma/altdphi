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
def dump_float(v):
    module_name = type(v).__module__
    class_name = v.__class__.__name__
    if module_name in ('__builtin__', 'builtins'):
        return "{}('{!r}')".format(class_name, v)

    if module_name == np.__name__:
        module_name = 'np'

    if module_name == 'np':
        special = dump_special_np_float(v)
        if special is not None:
            return special

    return "{}.{}('{!r}')".format(module_name, class_name, v)

##__________________________________________________________________||
def dump_special_np_float(v):
    specials =(
        'np.float64(np.pi)',
        'np.float64(np.pi/2)',
        'np.float64(np.pi/4)',
    )

    for s in specials:
        if v == eval(s):
            return s

    return None

##__________________________________________________________________||
