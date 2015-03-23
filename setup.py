from setuptools import (setup, find_packages)
from codecs import open  # To use a consistent encoding
from os import path


here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='vbox',
    version='9.9.9',
    description="VirtualBox CLI bindings",
    long_description=long_description,
    author="Ilja Orlovs",
    author_email="vywn@gryyf.fb".decode("rot13"),
    url='https://github.com/VRGhost/vbox',
    packages=find_packages('src', exclude=['tests']),
    package_dir={'': 'src'},
    install_requires=['psutil'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ])
