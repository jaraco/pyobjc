import Metal
from PyObjCTools.TestSupport import TestCase


class TestMTLVertexDescriptor(TestCase):
    def test_constants(self):
        self.assertEqual(Metal.MTLVertexFormatInvalid, 0)
        self.assertEqual(Metal.MTLVertexFormatUChar2, 1)
        self.assertEqual(Metal.MTLVertexFormatUChar3, 2)
        self.assertEqual(Metal.MTLVertexFormatUChar4, 3)
        self.assertEqual(Metal.MTLVertexFormatChar2, 4)
        self.assertEqual(Metal.MTLVertexFormatChar3, 5)
        self.assertEqual(Metal.MTLVertexFormatChar4, 6)
        self.assertEqual(Metal.MTLVertexFormatUChar2Normalized, 7)
        self.assertEqual(Metal.MTLVertexFormatUChar3Normalized, 8)
        self.assertEqual(Metal.MTLVertexFormatUChar4Normalized, 9)
        self.assertEqual(Metal.MTLVertexFormatChar2Normalized, 10)
        self.assertEqual(Metal.MTLVertexFormatChar3Normalized, 11)
        self.assertEqual(Metal.MTLVertexFormatChar4Normalized, 12)
        self.assertEqual(Metal.MTLVertexFormatUShort2, 13)
        self.assertEqual(Metal.MTLVertexFormatUShort3, 14)
        self.assertEqual(Metal.MTLVertexFormatUShort4, 15)
        self.assertEqual(Metal.MTLVertexFormatShort2, 16)
        self.assertEqual(Metal.MTLVertexFormatShort3, 17)
        self.assertEqual(Metal.MTLVertexFormatShort4, 18)
        self.assertEqual(Metal.MTLVertexFormatUShort2Normalized, 19)
        self.assertEqual(Metal.MTLVertexFormatUShort3Normalized, 20)
        self.assertEqual(Metal.MTLVertexFormatUShort4Normalized, 21)
        self.assertEqual(Metal.MTLVertexFormatShort2Normalized, 22)
        self.assertEqual(Metal.MTLVertexFormatShort3Normalized, 23)
        self.assertEqual(Metal.MTLVertexFormatShort4Normalized, 24)
        self.assertEqual(Metal.MTLVertexFormatHalf2, 25)
        self.assertEqual(Metal.MTLVertexFormatHalf3, 26)
        self.assertEqual(Metal.MTLVertexFormatHalf4, 27)
        self.assertEqual(Metal.MTLVertexFormatFloat, 28)
        self.assertEqual(Metal.MTLVertexFormatFloat2, 29)
        self.assertEqual(Metal.MTLVertexFormatFloat3, 30)
        self.assertEqual(Metal.MTLVertexFormatFloat4, 31)
        self.assertEqual(Metal.MTLVertexFormatInt, 32)
        self.assertEqual(Metal.MTLVertexFormatInt2, 33)
        self.assertEqual(Metal.MTLVertexFormatInt3, 34)
        self.assertEqual(Metal.MTLVertexFormatInt4, 35)
        self.assertEqual(Metal.MTLVertexFormatUInt, 36)
        self.assertEqual(Metal.MTLVertexFormatUInt2, 37)
        self.assertEqual(Metal.MTLVertexFormatUInt3, 38)
        self.assertEqual(Metal.MTLVertexFormatUInt4, 39)
        self.assertEqual(Metal.MTLVertexFormatInt1010102Normalized, 40)
        self.assertEqual(Metal.MTLVertexFormatUInt1010102Normalized, 41)
        self.assertEqual(Metal.MTLVertexFormatUChar4Normalized_BGRA, 42)
        self.assertEqual(Metal.MTLVertexFormatUChar, 45)
        self.assertEqual(Metal.MTLVertexFormatChar, 46)
        self.assertEqual(Metal.MTLVertexFormatUCharNormalized, 47)
        self.assertEqual(Metal.MTLVertexFormatCharNormalized, 48)
        self.assertEqual(Metal.MTLVertexFormatUShort, 49)
        self.assertEqual(Metal.MTLVertexFormatShort, 50)
        self.assertEqual(Metal.MTLVertexFormatUShortNormalized, 51)
        self.assertEqual(Metal.MTLVertexFormatShortNormalized, 52)
        self.assertEqual(Metal.MTLVertexFormatHalf, 53)

        self.assertEqual(Metal.MTLVertexStepFunctionConstant, 0)
        self.assertEqual(Metal.MTLVertexStepFunctionPerVertex, 1)
        self.assertEqual(Metal.MTLVertexStepFunctionPerInstance, 2)
        self.assertEqual(Metal.MTLVertexStepFunctionPerPatch, 3)
        self.assertEqual(Metal.MTLVertexStepFunctionPerPatchControlPoint, 4)
