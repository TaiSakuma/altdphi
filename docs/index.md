[![](https://badge.fury.io/py/altdphi.svg)](https://badge.fury.io/py/altdphi) [![](https://anaconda.org/conda-forge/altdphi/badges/version.svg)](https://anaconda.org/conda-forge/altdphi) [![](https://readthedocs.org/projects/altdphi/badge/?version=latest)](https://altdphi.readthedocs.io/en/latest/?badge=latest) [![](https://travis-ci.org/TaiSakuma/altdphi.svg?branch=master)](https://travis-ci.org/TaiSakuma/altdphi) [![](https://codecov.io/gh/TaiSakuma/altdphi/branch/master/graph/badge.svg)](https://codecov.io/gh/TaiSakuma/altdphi)

# altdphi

A Python library for calculating alternative angular variables to
\\(\Delta\varphi\\) and \\(\Delta\varphi^*\\) in new physics searches
with missing transverse momentum at LHC.

*****

- [1. Introduction](#introduction)
- [2. Requirement](#requirement)
- [3. Install](#install)
- [4. How to use](#how-to-use)
- [<i class="fa fa-check fa-fw"></i> License](#i-class-fa-fa-check-fa-fw-i-license)
- [<i class="fa fa-envelope fa-fw"></i> Contact](#i-class-fa-fa-envelope-fa-fw-i-contact)

*****

## 1. Introduction

The python library *altdphi* contains code to calculate the
alternative angular variables for suppression of QCD multijet events
in SUSY searches at LHC. The variables are described in
[arXiv:1803.07942](https://arxiv.org/abs/1803.07942). This page
quickly explains how to use altdphi.

*****

## 2. Requirement

- Python 2.7, 3.6, 3.7
- [NumPy](http://www.numpy.org/)

*****

## 3. Install

You can install with `conda` from conda-forge or `pip`, create a clone
with `git` from github, or just copy one file from github.

### with conda

```bash
conda install -c conda-forge altdphi
```

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

### just copy one file

The implementation for calculating the variables is contained in one
file. So, instead of checking out the whole package, you can just copy
one file.

- [altdphi.py](https://github.com/TaiSakuma/altdphi/blob/master/altdphi/altdphi.py)

Place the file *altdphi.py* where python can find.


*****

## 4. How to use

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
example on this page works as shown.

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
And their \\(p\_{\text{T}i}\\) are `741.63`, `498.69`,
and `45.62` GeV. And their \\(\varphi_i\\) are `-1.41`,  `1.81`, and `0.92` rad.
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

If you just print the object, it will show more variables:

```python
>>> print(alt)
AltDphi(pt=array([ 741.63,  498.69,   45.62]), phi=array([-1.41,  1.81,  0.92])):
                   pt: [ 741.63  498.69   45.62]
                  phi: [-1.41  1.81  0.92]
                  mht: 213.153450542
              mht_phi: 1.70358629053
                max_f: 3.47932439336
      min_omega_tilde: 0.00804814218906
        min_omega_hat: 0.0453671227463
              min_chi: 0.0112922228279
        min_dphi_star: 0.0112922228279
                   xi: 0.0112922228279
    min_minimized_mht: 5.96887256535
                min_X: 2.40707857323
                    f: [ 3.47932439  2.33958211  0.21402422]
                 dphi: [ 3.11358629  0.10641371  0.78358629]
                omega: [ 0.00804814  0.04536712  1.27638267]
          omega_tilde: [ 0.00804814  0.04536712  1.27638267]
            omega_hat: [ 0.27986865  0.04536712  1.27638267]
                  chi: [ 0.01129222  0.04536712  1.27638267]
            dphi_star: [ 0.01129222  0.03184746  0.65315528]
       sin_dphi_tilde: [ 0.0280027   0.10621299  0.70582443]
                    g: [ 2.47971655  3.33392551  0.92241102]
        minimized_mht: [   5.96887257   22.63966471  150.4489135 ]
                    X: [   2.40707857    9.67679852  702.9527629 ]
```

### Use MET instead of MHT

In the above example, the `AltDphi` object was initialized only with
`pt` and `phi`. The MHT was automatically calculated based on the `pt`
and `phi`. `AltDphi` has optional arguments `mht`, `mht_phi`. You can
specify the values of MHT with these optional arguments. For example,
you can give the values of MET to these arguments, which is useful,
for example, if the event contains a lepton or photon.

We are still using the same event. Suppose this event has MET =
`264.16` GeV and its \\(\varphi\\) is `1.44` rad.

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

Now, you can obtain the values of the variables calculated based on
MET in the place of MHT.

```python
>>> print(alt)
AltDphi(pt=array([ 741.63,  498.69,   45.62]), phi=array([-1.41,  1.81,  0.92]), mht=264.16, mht_phi=1.44):
                   pt: [ 741.63  498.69   45.62]
                  phi: [-1.41  1.81  0.92]
                  mht: 264.16
              mht_phi: 1.44
                max_f: 2.80750302847
      min_omega_tilde: 0.102040691243
        min_omega_hat: 0.189258023626
              min_chi: 0.154183878088
        min_dphi_star: 0.127529232391
                   xi: 0.151118397198
    min_minimized_mht: 75.9401917404
                min_X: 41.0550594385
                    f: [ 2.80750303  1.88783313  0.17269836]
                 dphi: [ 2.85  0.37  0.52]
                omega: [ 0.10204069  0.18925802  1.23629202]
          omega_tilde: [ 0.10204069  0.18925802  1.23629202]
            omega_hat: [ 0.34217719  0.18925802  1.23629202]
                  chi: [ 0.15418388  0.18925802  1.23629202]
            dphi_star: [ 0.15418388  0.12752923  0.44551197]
       sin_dphi_tilde: [ 0.28747801  0.36161543  0.49688014]
                    g: [ 1.84971579  2.82016048  1.04051754]
        minimized_mht: [  75.94019174   95.52433251  131.25585721]
                    X: [  41.05505944   50.59998732  760.02953181]
```

*****

## <i class="fa fa-check fa-fw"></i> License

altdphi is licensed under the BSD license.

*****

## <i class="fa fa-envelope fa-fw"></i> Contact

- Tai Sakuma - tai.sakuma@gmail.com


<br />
<br />
