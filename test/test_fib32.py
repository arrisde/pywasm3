import unittest
import os

from pywasm3._pywasm3 import lib, ffi


class TestFib32(unittest.TestCase):

    def test_fib32_32(self):
        env = lib.m3_NewEnvironment()
        runtime_p = lib.m3_NewRuntime(env, 64*1024, ffi.NULL)

        with open(os.path.join(os.path.dirname(__file__), "fib32.wasm"), "rb") as binary_file:
            wasm = binary_file.read()

        module_p = ffi.new("IM3Module *")
        res = lib.m3_ParseModule(env, module_p, wasm, len(wasm))
        self.assertEqual(res, ffi.NULL, "Should parse fib32.wasm module")

        res = lib.m3_LoadModule(runtime_p, module_p[0])
        self.assertEqual(res, ffi.NULL, "Should load fib32.wasm module")

        function_p = ffi.new("IM3Function *")
        res = lib.m3_FindFunction(function_p, runtime_p, "fib".encode())
        self.assertEqual(res, ffi.NULL, "Should locate fib function")

        argv_keepalive = [ffi.new("char[]", "32".encode())]
        argv = ffi.new("char *[]", argv_keepalive)
        res = lib.m3_CallWithArgs(function_p[0], 1, argv)
        self.assertEqual(res, ffi.NULL, "Should be able to execute fib(32)")

        res = lib.m3_GetResultI32(runtime_p)
        self.assertEqual(res, 2178309, "fib(32) should equal 2178309")



