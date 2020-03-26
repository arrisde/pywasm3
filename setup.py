import sys
from skbuild import setup

setup(
    name="pywasm3",
    version="0.1",
    description="Python 3 bindings for wasm3",
    author='arrisde',
    license="MIT",
    packages=['pywasm3'],
    install_requires=["cffi==1.14.0"]
)
