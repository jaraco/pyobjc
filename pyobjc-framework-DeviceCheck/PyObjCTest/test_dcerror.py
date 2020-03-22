import sys

from PyObjCTools.TestSupport import TestCase

if sys.maxsize > 2 ** 32:
    import DeviceCheck

    class TestDCError(TestCase):
        def test_constants(self):
            self.assertIsInstance(DeviceCheck.DCErrorDomain, str)

            self.assertEqual(DeviceCheck.DCErrorUnknownSystemFailure, 0)
            self.assertEqual(DeviceCheck.DCErrorFeatureUnsupported, 1)
