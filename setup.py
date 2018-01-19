from setuptools import setup, find_packages

import versioneer

setup(
    name = 'altdphi',
    version = versioneer.get_version(),
    cmdclass = versioneer.get_cmdclass(),
    description = 'A Python library for calculating alternative angular variables to Delta phi in SUSY searches at LHC',
    author = 'Tai Sakuma',
    author_email = 'tai.sakuma@gmail.com',
    url = 'https://github.com/TaiSakuma/altdphi',
    packages = find_packages(exclude=['docs', 'tests']),
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ]
)
