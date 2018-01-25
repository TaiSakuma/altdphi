
# altdphi
A Python library for calculating alternative angular variables to
Delta phi in SUSY searches at LHC


## Install

```python
pip install altdphi
```

## How to use

```python
import numpy as np
from altdphi import AltDphi


pt = np.array([741.63,  498.69, 45.62])
phi = np.array([-1.41,  1.81, 0.92])

alt = AltDphi(pt=pt, phi=phi)

alt.min_omega_tilde
alt.min_omega_hat
alt.min_chi
```
