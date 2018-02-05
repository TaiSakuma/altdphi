
# altdphi
A Python library for calculating alternative angular variables to
\\(\Delta\varphi\\) in SUSY searches at LHC

---

- [Introduction](#introduction)
- [Requirement](#requirement)
- [Install](#install)
    - [with pip](#with-pip)
    - [with git](#with-git)
- [How to use](#how-to-use)
    - [Launch python and import libraries](#launch-python-and-import-libraries)
    - [A simple example](#a-simple-example)
    - [Use MET instead of MHT](#use-met-instead-of-mht)

---

## Introduction

The python library *altdphi* contains code to calculate the
alternative angular variables for suppression of QCD multijet events
in SUSY searches at LHC. The variables are introduced in
arXiv:18xx.xxxxx. This page quickly explains how to use altdphi.

---

## Requirement

- Python 2.7 or 3.6
- [NumPy](http://www.numpy.org/)

---

## Install

You can install with `pip` or create a clone with `git` from github.

### with pip


```bash
$ pip install altdphi
```

### with git

```bash
$ git clone git@github.com:TaiSakuma/altdphi.git
```

If you install with `git`, you will probably need to set the
environment variable `PYTHONPATH` so that python can find `altdphi`.
To do this, for example, in bash, you can execute the following
command in the same directory you ran `git clone` command.


```bash
$ export PYTHONPATH=$PWD/altdphi:$PYTHONPATH
```

---

## How to use

Here, we will quickly shows how to use altdphi interactively as an example.

### Launch python and import libraries

Start python:
```bash
$ python
Python 3.6.3 |Anaconda, Inc.| (default, Nov  8 2017, 18:10:31) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

This example uses python 3. If you are using python 2, you can import
`print_function` from ` __future__` so that the `print` command in the
example works as shown.

```python
>>> from __future__ import print_function
```

Import `numpy` and `altdphi`:
```python
>>> import numpy as np
>>> from altdphi import AltDphi
```

We are ready to start using altdphi.

### A simple example

Suppose an event has three jets.
And their \\(p\_{\text{T}i}\\) are 741.63, 498.69,
and 45.62 GeV. And their \\(\varphi_i\\) are -1.41,  1.81, and 0.92 rad.
You can define them as numpy arrays as follows:
```python
>>> pt = np.array([741.63, 498.69, 45.62])
>>> phi = np.array([-1.41, 1.81, 0.92])
```

With these numpy arrays, you can create an `AltDphi` object:

```python
>>> alt = AltDphi(pt=pt, phi=phi)
```

You can access to the three alternative variables,
\\(\tilde{\omega}\_\text{min}\\), \\(\hat{\omega}\_\text{min}\\), and
\\(\chi\_\text{min}\\), as attributes of this object.

```python
>>> alt.min_omega_tilde
0.0080481421890630823
>>> alt.min_omega_hat
0.045367122746276765
>>> alt.min_chi
0.011292222827857776
```
Inatead of the minima, you can also access to these angles for each jet
as numpy arrays.

```python
>>> alt.omega_tilde
array([ 0.00804814,  0.04536712,  1.27638267])
>>> alt.omega_hat
array([ 0.27986865,  0.04536712,  1.27638267])
>>> alt.chi
array([ 0.01129222,  0.04536712,  1.27638267])
```

You can print all available variables as follows:

```python
>>> print(alt)
AltDphi(pt=array([ 741.63,  498.69,   45.62]), phi=array([-1.41,  1.81,  0.92])):
                    pt: [ 741.63  498.69   45.62]
                   phi: [-1.41  1.81  0.92]
                    px: [ 118.73816058 -118.15414729   27.63751555]
                    py: [-732.06304791  484.4907776    36.29534591]
                  mhtx: -28.2215288359
                  mhty: 211.27692441
                   mht: 213.153450542
              cos_dphi: [-0.99960785  0.9943434   0.70838681]
              sin_dphi: [ 0.0280027   0.10621299  0.70582443]
                  dphi: [ 3.11358629  0.10641371  0.78358629]
                     f: [ 3.47932439  2.33958211  0.21402422]
              arccot_f: [ 0.27986865  0.40392434  1.35995303]
             dphi_star: [ 0.01129222  0.03184746  0.65315528]
        sin_dphi_tilde: [ 0.0280027   0.10621299  0.70582443]
            dphi_tilde: [ 3.11358629  0.10641371  0.78358629]
                     g: [ 2.47971655  3.33392551  0.92241102]
                 omega: [ 0.00804814  0.04536712  1.27638267]
           omega_tilde: [ 0.00804814  0.04536712  1.27638267]
          sin_dphi_hat: [ 1.          0.10621299  0.70582443]
              dphi_hat: [ 1.57079633  0.10641371  0.78358629]
             omega_hat: [ 0.27986865  0.04536712  1.27638267]
                     k: [ 2.47971655  2.33958211  0.21402422]
                   chi: [ 0.01129222  0.04536712  1.27638267]
                     h: [ 2.47971655  2.33958211  0.21402422]
       min_omega_tilde: 0.00804814218906
         min_omega_hat: 0.0453671227463
               min_chi: 0.0112922228279
         min_dphi_star: 0.0112922228279
             min_omega: 0.00804814218906
        min_dphi_tilde: 0.106413709473
    min_sin_dphi_tilde: 0.0280027020448
                 max_f: 3.47932439336
                 max_h: 2.47971654592
                    xi: 0.0112922228279
```

### Use MET instead of MHT

In the above example, the `AltDphi` object was initialized with `pt`
and `phi`. MHT was calculated based on the `pt` and `phi`. `AltDphi`
has optional arguments `mht`, `mht_phi`. You can specify the values of
MHT with these optional arguments. For example, you can give the
values of MET to these arguments, which is useful, for example, if the
event contains a lepton or photon.

We are still using the same event. Suppose, this event has MET =
264.16 GeV and its \\(\varphi\\) is 1.44 rad.

```python
>>> pt = np.array([741.63, 498.69, 45.62])
>>> phi = np.array([-1.41, 1.81, 0.92])
>>> met = 264.16
>>> met_phi = 1.44
```

Then, you can create and an `AltDphi` object as follows:

```python
>>> alt = AltDphi(pt=pt, phi=phi, mht=met, mht_phi=met_phi)
```

You can obtain the values of the variables calculated based on MET in
the place of MHT.

```python
>>> print(alt)
AltDphi(pt=array([ 741.63,  498.69,   45.62]), phi=array([-1.41,  1.81,  0.92])):
                    pt: [ 741.63  498.69   45.62]
                   phi: [-1.41  1.81  0.92]
                    px: [ 118.73816058 -118.15414729   27.63751555]
                    py: [-732.06304791  484.4907776    36.29534591]
                  mhtx: 34.4527269003
                  mhty: 261.903637258
                   mht: 264.16
              cos_dphi: [-0.95778724  0.93232735  0.86781918]
              sin_dphi: [ 0.28747801  0.36161543  0.49688014]
                  dphi: [ 2.85  0.37  0.52]
                     f: [ 2.80750303  1.88783313  0.17269836]
              arccot_f: [ 0.34217719  0.48713046  1.39978477]
             dphi_star: [ 0.15418388  0.12752923  0.44551197]
        sin_dphi_tilde: [ 0.28747801  0.36161543  0.49688014]
            dphi_tilde: [ 2.85  0.37  0.52]
                     g: [ 1.84971579  2.82016048  1.04051754]
                 omega: [ 0.10204069  0.18925802  1.23629202]
           omega_tilde: [ 0.10204069  0.18925802  1.23629202]
          sin_dphi_hat: [ 1.          0.36161543  0.49688014]
              dphi_hat: [ 1.57079633  0.37        0.52      ]
             omega_hat: [ 0.34217719  0.18925802  1.23629202]
                     k: [ 1.84971579  1.88783313  0.17269836]
                   chi: [ 0.15418388  0.18925802  1.23629202]
                     h: [ 1.84971579  1.88783313  0.17269836]
       min_omega_tilde: 0.102040691243
         min_omega_hat: 0.189258023626
               min_chi: 0.154183878088
         min_dphi_star: 0.127529232391
             min_omega: 0.102040691243
        min_dphi_tilde: 0.37
    min_sin_dphi_tilde: 0.287478012343
                 max_f: 2.80750302847
                 max_h: 1.88783313144
                    xi: 0.151118397198
```


<br />
<br />
