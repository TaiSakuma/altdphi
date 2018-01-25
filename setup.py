from setuptools import setup, find_packages
import os
import versioneer

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name='altdphi',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='A Python library for calculating alternative angular variables to Delta phi in SUSY searches at LHC',
    long_description=long_description,
    description_content_type='text/markdown',
    author='Tai Sakuma',
    author_email='tai.sakuma@gmail.com',
    url='https://github.com/TaiSakuma/altdphi',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(exclude=['docs', 'tests']),
)
