import os
import cffi
import sys

cffi_includes = ["stack_accessor.h"]


def build_cffi(src_in: str, src_out: str) -> None:
    ffiBuilder = cffi.FFI()

    cffi_includes.insert(0, src_in)

    for include_file in cffi_includes:
        if os.path.isabs(include_file):
            include_file_abs = include_file
        else:
            include_file_abs = os.path.join(os.path.dirname(__file__), include_file)

        with open(include_file_abs) as f:
            ffiBuilder.cdef(f.read())

    #cffi_includes.insert(0, src_in)
    code_lines = [f'#include "{f}"' for f in cffi_includes]
    cffi_code = '\n'.join(code_lines)

    ffiBuilder.set_source("_pywasm3",
        # Since we are calling a fully built library directly no custom source
        # is necessary. We need to include the .h files, though, because behind
        # the scenes cffi generates a .c file which contains a Python-friendly
        # wrapper around each of the functions.
        cffi_code,
        # The important thing is to include the pre-built lib in the list of
        # libraries we are linking against:
        include_dirs=[os.path.dirname(__file__)],
        #libraries=["pywasm3"],
        #library_dirs=[os.path.dirname(__file__),],
    )

    ffiBuilder.emit_c_code(outfile)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        infile = sys.argv[1]
    else:
        infile = os.path.join(os.path.dirname(__file__), "_wasm3.h")

    if len(sys.argv) > 2:
        outfile = sys.argv[2]
    else:
        outfile = os.path.join(os.path.dirname(__file__), "_pywasm3_cffi.c")

    build_cffi(infile, outfile)
