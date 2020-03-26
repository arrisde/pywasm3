# pywasm3

Python 3 bindings to [wasm3](https://github.com/wasm3/wasm3) generated by [CFFI](https://cffi.readthedocs.io). 

## Prerequisites
- CPython >= 3.5
- CMake >= 3.4.0
- C compiler that can build wasm3 (e.g. GCC, Clang, MSVC); see [Wasm3 development notes](https://github.com/wasm3/wasm3/blob/master/docs/Development.md)
- A build tool supported by CMake, e.g. GNU make, Ninja, VS2017

## Build
- Create a virtual environment and install dependencies:
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
- Build pywasm3:
```
python setup.py develop
```

## Run tests
```
python -m unittest discover
```

## Notes
- Currently pywasm3 consists of CFFI glue code for calling wasm3 from Python, it does not implement a Python-friendly API. See the test code and [CFFI docs](https://cffi.readthedocs.io/en/latest/using.html) for how to invoke wasm3 functions from Python. 