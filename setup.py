from setuptools import (setup, find_packages)

setup(
    name='vbox',
    version='0.2.5',
    description="VirtualBox CLI bindings",
    long_description=open("README.rst").read(),

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
