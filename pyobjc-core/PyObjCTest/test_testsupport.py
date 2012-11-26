from PyObjCTools.TestSupport import *
import unittest
import objc
import sys

from PyObjCTools import TestSupport

class Method(object):
    def __init__(self, argno, meta, selector=False):
        self._selector = selector
        if argno is None:
            self._meta = {'retval': meta}
        else:
            self._meta = {'arguments': { argno: meta }}

    @property
    def __class__(self):
        if self._selector:
            return objc.selector

        else:
            return Method
        

    def __metadata__(self):
        return self._meta.copy()


class TestTestSupport (TestCase):

    def test_sdkForPython(self):
        orig_get_config_var = TestSupport._get_config_var
        try:
            config_result = ''
            def get_config_var(value):
                if value != 'CFLAGS':
                    raise KeyError(value)

                return config_result

            TestSupport._get_config_var = get_config_var
            cache = sdkForPython.func_defaults[0]

            config_result = ''
            self.assertEqual(sdkForPython(), None)
            self.assertEqual(cache, [None])
            self.assertEqual(sdkForPython(), None)
            self.assertEqual(cache, [None])

            cache[:] = []

            config_result = '-isysroot /Developer/SDKs/MacOSX10.6.sdk'
            self.assertEqual(sdkForPython(), (10, 6))
            self.assertEqual(cache, [(10,6)])
            self.assertEqual(sdkForPython(), (10, 6))
            self.assertEqual(cache, [(10,6)])

            cache[:] = []

            config_result = '-isysroot /'
            os_rel = tuple(map(int, os_release().split('.')))
            self.assertEqual(sdkForPython(), os_rel)
            self.assertEqual(cache, [os_rel])
            self.assertEqual(sdkForPython(), os_rel)
            self.assertEqual(cache, [os_rel])

            cache[:] = []

            config_result = '-dynamic -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.4u.sdk -arch i386 -arch x86_64'
            self.assertEqual(sdkForPython(), (10,4))
            self.assertEqual(cache, [(10,4)])
            self.assertEqual(sdkForPython(), (10,4))
            self.assertEqual(cache, [(10,4)])

            cache[:] = []

            config_result = '-dynamic -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.10.sdk -arch i386 -arch x86_64'
            self.assertEqual(sdkForPython(), (10,10))
            self.assertEqual(cache, [(10,10)])
            self.assertEqual(sdkForPython(), (10,10))
            self.assertEqual(cache, [(10,10)])

            cache[:] = []

        finally:
            TestSupport._get_config_var = orig_get_config_var

    def test_os_release(self):
        import platform
        TestSupport._os_release = '10.10'
        self.assertEqual(os_release(), '10.10')
        TestSupport._os_release = None

        self.assertEqual(TestSupport.os_release(), '.'.join(platform.mac_ver()[0].split('.')[:2]))

    def test_fourcc(self):
        import struct
        self.assertEqual(fourcc('abcd'), struct.unpack('>i', 'abcd')[0])

    def testIs32Bit(self):
        orig = sys.maxsize
        try:
            sys.maxsize = 2 ** 31 -1
            self.assertTrue(is32Bit())

            sys.maxsize = 2 ** 63 -1
            self.assertFalse(is32Bit())

        finally:
            sys.maxsize = orig


    def test_assert_opaque(self):
        self.assertRaises(AssertionError, self.assertIsOpaquePointer, long)

        class N (object):
            @property
            def __pointer__(self):
                pass

        self.assertRaises(AssertionError, self.assertIsOpaquePointer, N)

        class N (object):
            __typestr__  = b"^q"

        self.assertRaises(AssertionError, self.assertIsOpaquePointer, N)

        class N (object):
            __typestr__  = b"^q"

            @property
            def __pointer__(self):
                pass

        try:
            self.assertIsOpaquePointer(N)

        except AssertionError:
            self.fail("assertIsOpaque fails on opaque pointer type")



    def test_assert_arg_IN(self):
        m = Method(3, { "type": b"n^@" })
        try:
            self.assertArgIsIn(m, 3)
        except AssertionError:
            raise
            self.fail("test failure for input argument")

        m = Method(3, { "type": b"n^@" }, selector=True)
        try:
            self.assertArgIsIn(m, 1)
        except AssertionError:
            self.fail("test failure for input argument")

        m = Method(3, { "type": b"^@" })
        try:
            self.assertArgIsIn(m, 3)
        except AssertionError:
            pass
        else:
            self.fail("test pass for not-input argument")

        m = Method(3, { "type": b"^@" }, selector=True)
        try:
            self.assertArgIsIn(m, 1)
        except AssertionError:
            pass

        else:
            self.fail("test pass for not-input argument")

    def test_assert_arg_OUT(self):
        m = Method(3, { "type": b"o^@" })
        try:
            self.assertArgIsOut(m, 3)
        except AssertionError:
            raise
            self.fail("test failure for input argument")

        m = Method(3, { "type": b"o^@" }, selector=True)
        try:
            self.assertArgIsOut(m, 1)
        except AssertionError:
            self.fail("test failure for input argument")

        m = Method(3, { "type": b"^@" })
        try:
            self.assertArgIsOut(m, 3)
        except AssertionError:
            pass
        else:
            self.fail("test pass for not-input argument")

        m = Method(3, { "type": b"^@" }, selector=True)
        try:
            self.assertArgIsOut(m, 1)
        except AssertionError:
            pass

        else:
            self.fail("test pass for not-input argument")

    def test_assert_arg_INOUT(self):
        m = Method(3, { "type": b"N^@" })
        try:
            self.assertArgIsInOut(m, 3)
        except AssertionError:
            raise
            self.fail("test failure for input argument")

        m = Method(3, { "type": b"N^@" }, selector=True)
        try:
            self.assertArgIsInOut(m, 1)
        except AssertionError:
            self.fail("test failure for input argument")

        m = Method(3, { "type": b"^@" })
        try:
            self.assertArgIsInOut(m, 3)
        except AssertionError:
            pass
        else:
            self.fail("test pass for not-input argument")

        m = Method(3, { "type": b"^@" }, selector=True)
        try:
            self.assertArgIsInOut(m, 1)
        except AssertionError:
            pass

        else:
            self.fail("test pass for not-input argument")

    def test_arg_bool(self):
        m = Method(3, { "type": objc._C_NSBOOL })
        try:
            self.assertArgIsBOOL(m, 3)
        except AssertionError:
            raise
            self.fail("unexpected test failure")

        m = Method(3, { "type": objc._C_NSBOOL }, selector=True)
        try:
            self.assertArgIsBOOL(m, 1)
        except AssertionError:
            self.fail("unexpected test failure")

        m = Method(3, { "type": b"@" })
        try:
            self.assertArgIsBOOL(m, 3)
        except AssertionError:
            pass
        else:
            self.fail("unexpected test pass")

        m = Method(3, { "type": b"@" }, selector=True)
        try:
            self.assertArgIsBOOL(m, 1)
        except AssertionError:
            pass

        else:
            self.fail("unexpected test pass")

    def test_result_bool(self):
        m = Method(None, { "type": objc._C_NSBOOL })
        try:
            self.assertResultIsBOOL(m)
        except AssertionError:
            raise
            self.fail("unexpected test failure")

        m = Method(None, { "type": objc._C_NSBOOL }, selector=True)
        try:
            self.assertResultIsBOOL(m)
        except AssertionError:
            self.fail("unexpected test failure")

        m = Method(None, { "type": b"@" })
        try:
            self.assertResultIsBOOL(m)
        except AssertionError:
            pass
        else:
            self.fail("unexpected test pass")

        m = Method(None, { "type": b"@" }, selector=True)
        try:
            self.assertResultIsBOOL(m)
        except AssertionError:
            pass

        else:
            self.fail("unexpected test pass")
        

    def run(self, *args, **kwds):
        unittest.TestCase.run(self, *args, **kwds)


if __name__ == "__main__":
    main()