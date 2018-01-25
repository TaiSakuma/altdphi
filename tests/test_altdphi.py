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
nojet = dict(
    pt =  [ ],
    phi = [ ],
)

monojet = dict(
    pt =  [1514.21],
    phi = [  -1.04],
)

two_jets = dict(
    pt =  [ 960.07,  665.01],
    phi = [  -0.79,    2.34],
)

three_jets = dict(
    pt =  [ 741.63,  498.69,   45.62],
    phi = [  -1.41,    1.81,    0.92],
)

four_jets = dict(
    pt =  [1149.61,  794.66,  251.60,   94.49],
    phi = [  -1.32,    2.75,    0.87,   -2.77],
)

##__________________________________________________________________||
## expected altdphi:
##   produced by dump_altdphi()
##   example how they were produced
##      from .dump import dump_altdphi
##      names = ['nojet', 'monojet', 'two_jets', 'three_jets', 'four_jets']
##      jet_dicts = [nojet, monojet, two_jets, three_jets, four_jets]
##
##      for n, jets in zip(names, jet_dicts):
##          pt = np.array(jets['pt'])
##          phi = np.array(jets['phi'])
##          altdphi = AltDphi(pt=pt, phi=phi)
##          dumped = dump_altdphi(altdphi)
##          print 'altdphi_{}={}'.format(n, dumped)

altdphi_nojet=mock.MagicMock(
    pt=np.array([]),
    phi=np.array([]),
    px=np.array([]),
    py=np.array([]),
    mhtx=np.float64(-0.0),
    mhty=np.float64(-0.0),
    mht=np.float64(0.0),
    cos_dphi=np.array([]),
    sin_dphi=np.array([]),
    dphi=np.array([]),
    f=np.array([]),
    arccot_f=np.array([]),
    dphi_star=np.array([]),
    sin_dphi_tilde=np.array([]),
    dphi_tilde=np.array([]),
    g=np.array([]),
    omega=np.array([]),
    omega_tilde=np.array([]),
    sin_dphi_hat=np.array([]),
    dphi_hat=np.array([]),
    omega_hat=np.array([]),
    k=np.array([]),
    chi=np.array([]),
    h=np.array([]),
    min_omega_tilde=np.nan,
    min_omega_hat=np.nan,
    min_chi=np.nan,
    min_dphi_star=np.nan,
    min_omega=np.nan,
    min_dphi_tilde=np.nan,
    min_sin_dphi_tilde=np.nan,
    max_f=np.nan,
    max_h=np.nan,
    xi=np.nan,
    varnames=('pt', 'phi', 'px', 'py', 'mhtx', 'mhty', 'mht', 'cos_dphi', 'sin_dphi', 'dphi', 'f', 'arccot_f', 'dphi_star', 'sin_dphi_tilde', 'dphi_tilde', 'g', 'omega', 'omega_tilde', 'sin_dphi_hat', 'dphi_hat', 'omega_hat', 'k', 'chi', 'h', 'min_omega_tilde', 'min_omega_hat', 'min_chi', 'min_dphi_star', 'min_omega', 'min_dphi_tilde', 'min_sin_dphi_tilde', 'max_f', 'max_h', 'xi')
)
altdphi_monojet=mock.MagicMock(
    pt=np.array([1514.21]),
    phi=np.array([-1.04]),
    px=np.array([766.52377570444537]),
    py=np.array([-1305.8611049341355]),
    mhtx=np.float64(-766.523775704),
    mhty=np.float64(1305.86110493),
    mht=np.float64(1514.21),
    cos_dphi=np.array([-1.0]),
    sin_dphi=np.array([0.0]),
    dphi=np.array([3.1415926535897931]),
    f=np.array([1.0]),
    arccot_f=np.array([0.78539816339744828]),
    dphi_star=np.array([1.5707963267948966]),
    sin_dphi_tilde=np.array([0.0]),
    dphi_tilde=np.array([3.1415926535897931]),
    g=np.array([0.0]),
    omega=np.array([0.0]),
    omega_tilde=np.array([0.0]),
    sin_dphi_hat=np.array([1.0]),
    dphi_hat=np.array([1.5707963267948966]),
    omega_hat=np.array([0.78539816339744828]),
    k=np.array([0.0]),
    chi=np.array([1.5707963267948966]),
    h=np.array([0.0]),
    min_omega_tilde=np.float64(0.0),
    min_omega_hat=np.float64(0.785398163397),
    min_chi=np.float64(1.57079632679),
    min_dphi_star=np.float64(1.57079632679),
    min_omega=np.float64(0.0),
    min_dphi_tilde=np.float64(3.14159265359),
    min_sin_dphi_tilde=np.float64(0.0),
    max_f=np.float64(1.0),
    max_h=np.float64(0.0),
    xi=np.float64(1.57079632679),
    varnames=('pt', 'phi', 'px', 'py', 'mhtx', 'mhty', 'mht', 'cos_dphi', 'sin_dphi', 'dphi', 'f', 'arccot_f', 'dphi_star', 'sin_dphi_tilde', 'dphi_tilde', 'g', 'omega', 'omega_tilde', 'sin_dphi_hat', 'dphi_hat', 'omega_hat', 'k', 'chi', 'h', 'min_omega_tilde', 'min_omega_hat', 'min_chi', 'min_dphi_star', 'min_omega', 'min_dphi_tilde', 'min_sin_dphi_tilde', 'max_f', 'max_h', 'xi')
)
altdphi_two_jets=mock.MagicMock(
    pt=np.array([960.07000000000005, 665.00999999999999]),
    phi=np.array([-0.79000000000000004, 2.3399999999999999]),
    px=np.array([675.74077219824244, -462.55656773109445]),
    py=np.array([-681.98886624997272, 477.78627203889965]),
    mhtx=np.float64(-213.184204467),
    mhty=np.float64(204.202594211),
    mht=np.float64(295.205359905),
    cos_dphi=np.array([-0.9996589655889383, 0.99928906811576212]),
    sin_dphi=np.array([0.026114220602076285, 0.037700906412601924]),
    dphi=np.array([3.1154754639667503, 0.037709843212846594]),
    f=np.array([3.2522105977613536, 2.2527030004242166]),
    arccot_f=np.array([0.29830786347663868, 0.41777892069188194]),
    dphi_star=np.array([0.01159265358979026, 0.01159265358979443]),
    sin_dphi_tilde=np.array([0.026114220602078408, 0.037700906412600453]),
    dphi_tilde=np.array([3.1154754639667503, 0.037709843212846594]),
    g=np.array([2.2525516321724153, 3.2519920685399786]),
    omega=np.array([0.0080295105724628741, 0.016734290818619626]),
    omega_tilde=np.array([0.0080295105724635264, 0.016734290818618974]),
    sin_dphi_hat=np.array([1.0, 0.037700906412601341]),
    dphi_hat=np.array([1.5707963267948966, 0.037709843212846594]),
    omega_hat=np.array([0.29830786347663868, 0.016734290818619369]),
    k=np.array([2.2525516321724153, 2.2527030004242166]),
    chi=np.array([0.011592653589791202, 0.016734290818618974]),
    h=np.array([2.2525516321724153, 2.2527030004242166]),
    min_omega_tilde=np.float64(0.00802951057246),
    min_omega_hat=np.float64(0.0167342908186),
    min_chi=np.float64(0.0115926535898),
    min_dphi_star=np.float64(0.0115926535898),
    min_omega=np.float64(0.00802951057246),
    min_dphi_tilde=np.float64(0.0377098432128),
    min_sin_dphi_tilde=np.float64(0.0261142206021),
    max_f=np.float64(3.25221059776),
    max_h=np.float64(2.25270300042),
    xi=np.float64(0.0115918747022),
    varnames=('pt', 'phi', 'px', 'py', 'mhtx', 'mhty', 'mht', 'cos_dphi', 'sin_dphi', 'dphi', 'f', 'arccot_f', 'dphi_star', 'sin_dphi_tilde', 'dphi_tilde', 'g', 'omega', 'omega_tilde', 'sin_dphi_hat', 'dphi_hat', 'omega_hat', 'k', 'chi', 'h', 'min_omega_tilde', 'min_omega_hat', 'min_chi', 'min_dphi_star', 'min_omega', 'min_dphi_tilde', 'min_sin_dphi_tilde', 'max_f', 'max_h', 'xi')
)

altdphi_three_jets=mock.MagicMock(
    pt=np.array([741.63, 498.69, 45.619999999999997]),
    phi=np.array([-1.4099999999999999, 1.8100000000000001, 0.92000000000000004]),
    px=np.array([118.73816057840951, -118.15414728856041, 27.637515546074777]),
    py=np.array([-732.06304791490186, 484.49077759903042, 36.295345906059019]),
    mhtx=np.float64(-28.2215288359),
    mhty=np.float64(211.27692441),
    mht=np.float64(213.153450542),
    cos_dphi=np.array([-0.99960784744728226, 0.99434340212687955, 0.70838680740468862]),
    sin_dphi=np.array([0.028002702044818219, 0.10621298718491401, 0.70582443361999914]),
    dphi=np.array([3.1135862905270009, 0.10641370947300177, 0.78358629052699869]),
    f=np.array([3.4793243933637945, 2.3395821120054348, 0.21402421534357602]),
    arccot_f=np.array([0.27986864988087262, 0.40392433736017369, 1.359953025463273]),
    dphi_star=np.array([0.011292222827858576, 0.031847464820604139, 0.65315528325565864]),
    sin_dphi_tilde=np.array([0.028002702044816235, 0.10621298718491401, 0.70582443361999925]),
    dphi_tilde=np.array([3.1135862905270009, 0.10641370947300177, 0.78358629052699869]),
    g=np.array([2.4797165459165122, 3.3339255141323143, 0.9224110227482647]),
    omega=np.array([0.0080481421890636513, 0.045367122746276758, 1.2763826688175239]),
    omega_tilde=np.array([0.0080481421890630823, 0.045367122746276758, 1.2763826688175239]),
    sin_dphi_hat=np.array([1.0, 0.10621298718491402, 0.70582443361999914]),
    dphi_hat=np.array([1.5707963267948966, 0.10641370947300177, 0.78358629052699869]),
    omega_hat=np.array([0.27986864988087262, 0.045367122746276765, 1.2763826688175239]),
    k=np.array([2.4797165459165122, 2.3395821120054348, 0.21402421534357602]),
    chi=np.array([0.011292222827857776, 0.045367122746276758, 1.2763826688175239]),
    h=np.array([2.4797165459165122, 2.3395821120054348, 0.21402421534357602]),
    min_omega_tilde=np.float64(0.00804814218906),
    min_omega_hat=np.float64(0.0453671227463),
    min_chi=np.float64(0.0112922228279),
    min_dphi_star=np.float64(0.0112922228279),
    min_omega=np.float64(0.00804814218906),
    min_dphi_tilde=np.float64(0.106413709473),
    min_sin_dphi_tilde=np.float64(0.0280027020448),
    max_f=np.float64(3.47932439336),
    max_h=np.float64(2.47971654592),
    xi=np.float64(0.0112922228279),
    varnames=('pt', 'phi', 'px', 'py', 'mhtx', 'mhty', 'mht', 'cos_dphi', 'sin_dphi', 'dphi', 'f', 'arccot_f', 'dphi_star', 'sin_dphi_tilde', 'dphi_tilde', 'g', 'omega', 'omega_tilde', 'sin_dphi_hat', 'dphi_hat', 'omega_hat', 'k', 'chi', 'h', 'min_omega_tilde', 'min_omega_hat', 'min_chi', 'min_dphi_star', 'min_omega', 'min_dphi_tilde', 'min_sin_dphi_tilde', 'max_f', 'max_h', 'xi')
)

altdphi_four_jets=mock.MagicMock(
    pt=np.array([1149.6099999999999, 794.65999999999997, 251.59999999999999, 94.489999999999995]),
    phi=np.array([-1.3200000000000001, 2.75, 0.87, -2.77]),
    px=np.array([285.3049809740844, -734.50612820407343, 162.23835928558429, -88.041079732417174]),
    py=np.array([-1113.6445662469589, 303.29072394430585, 192.30516055561708, -34.309304562321863]),
    mhtx=np.float64(375.003867677),
    mhty=np.float64(652.357986309),
    mht=np.float64(752.461854896),
    cos_dphi=np.array([-0.71615893122277974, -0.12975723623280308, 0.98400806713788269, -0.77915049550790449]),
    sin_dphi=np.array([0.69793723588145506, 0.99154579301473744, 0.17812390015819937, 0.62683690490412802]),
    dphi=np.array([2.3690795310682202, 1.7009204689317798, 0.17907953106822067, 2.4641057761113663]),
    f=np.array([1.5277983761160019, 1.056080112006978, 0.33436910902896294, 0.12557447182888198]),
    arccot_f=np.array([0.57955780728027761, 0.75812966780482549, 1.2481138641164293, 1.4458757384975724]),
    dphi_star=np.array([0.71021952472978622, 0.8193930825034822, 0.134295237807354, 2.3770746548226431]),
    sin_dphi_tilde=np.array([0.69793723588145506, 0.99154579301473744, 0.17812390015819937, 0.90558606663191821]),
    dphi_tilde=np.array([2.3690795310682202, 1.7009204689317798, 0.17907953106822067, 2.0088332609016368]),
    g=np.array([0.81163944489322215, 0.92632287577417494, 1.3183771761668457, 0.0]),
    omega=np.array([0.42851548447499943, 0.75389193745234218, 0.4894768734555921, 1.3730831194727287]),
    omega_tilde=np.array([0.42851548447499943, 0.75389193745234218, 0.4894768734555921, 1.4330084665965359]),
    sin_dphi_hat=np.array([1.0, 1.0, 0.17812390015819929, 1.0]),
    dphi_hat=np.array([1.5707963267948966, 1.5707963267948966, 0.17907953106822067, 1.5707963267948966]),
    omega_hat=np.array([0.57955780728027761, 0.75812966780482549, 0.48947687345559188, 1.4458757384975724]),
    k=np.array([0.81163944489322215, 0.92632287577417494, 0.33436910902896294, 0.0]),
    chi=np.array([0.71021952472978622, 0.8193930825034822, 0.4894768734555921, 1.5707963267948966]),
    h=np.array([1.5277983761160019, 1.056080112006978, 1.3183771761668457, 0.12557447182888198]),
    min_omega_tilde=np.float64(0.428515484475),
    min_omega_hat=np.float64(0.489476873456),
    min_chi=np.float64(0.489476873456),
    min_dphi_star=np.float64(0.134295237807),
    min_omega=np.float64(0.428515484475),
    min_dphi_tilde=np.float64(0.179079531068),
    min_sin_dphi_tilde=np.float64(0.178123900158),
    max_f=np.float64(1.52779837612),
    max_h=np.float64(1.52779837612),
    xi=np.float64(0.116064624878),
    varnames=('pt', 'phi', 'px', 'py', 'mhtx', 'mhty', 'mht', 'cos_dphi', 'sin_dphi', 'dphi', 'f', 'arccot_f', 'dphi_star', 'sin_dphi_tilde', 'dphi_tilde', 'g', 'omega', 'omega_tilde', 'sin_dphi_hat', 'dphi_hat', 'omega_hat', 'k', 'chi', 'h', 'min_omega_tilde', 'min_omega_hat', 'min_chi', 'min_dphi_star', 'min_omega', 'min_dphi_tilde', 'min_sin_dphi_tilde', 'max_f', 'max_h', 'xi')
)

@pytest.mark.parametrize(
    'jets, expected', [
        pytest.param(nojet, altdphi_nojet, id='nojet'),
        pytest.param(monojet, altdphi_monojet, id='monojet'),
        pytest.param(two_jets, altdphi_two_jets, id='two_jets'),
        pytest.param(three_jets, altdphi_three_jets, id='three_jets'),
        pytest.param(four_jets, altdphi_four_jets, id='four_jets'),
    ]
)
def test_monojet(jets, expected):
    pt = np.array(jets['pt'])
    phi = np.array(jets['phi'])
    actual = AltDphi(pt=pt, phi=phi)

    assert_altdphi_equal(expected, actual)

##__________________________________________________________________||
