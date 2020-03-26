import sys
import re

std_includes = [
    "assert.h",
    "ctype.h",
    "errno.h",
    "float.h",
    "limits.h",
    "locale.h",
    "math.h",
    "setjmp.h",
    "signal.h",
    "stdarg.h",
    "stddef.h",
    "stdio.h",
    "stdlib.h",
    "string.h",
    "time.h",
    "iso646.h",
    "wchar.h",
    "wctype.h",
    "complex.h",
    "fenv.h",
    "inttypes.h",
    "stdbool.h",
    "stdint.h",
    "tgmath.h",
    "stdalign.h",
    "stdatomic.h",
    "stdnoreturn.h",
    "threads.h",
    "uchar.h"
]

# remove #includes referencing headers from std lib as 
# we don't want to generate ffi code for these
def remove_std_includes(infile: str, outfile: str) -> None:
    with open(infile, "r", encoding="utf8") as input:
        with open(outfile, "w", encoding="utf8") as output:
            for line in input:
                m = re.search("#include <(.+?)>", line)
                if m:
                    found = m.group(1)
                    print(found)
                    if found in std_includes:
                        output.write('//')
                
                output.write(line)



if __name__ == "__main__":
    if len(sys.argv) > 1:
        infile = sys.argv[1]
    else:
        infile = os.path.join(os.path.dirname(__file__), "wasm3_pp.h")

    if len(sys.argv) > 2:
        outfile = sys.argv[2]
    else:
        outfile = os.path.join(os.path.dirname(__file__), "_wasm3.h")

    remove_std_includes(infile, outfile)
