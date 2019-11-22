from PyObjCTools.TestSupport import *

import Metal

class TestMTLPixelFormat (TestCase):
    def test_constants(self):
        self.assertEqual(Metal.MTLPixelFormatInvalid, 0)
        self.assertEqual(Metal.MTLPixelFormatA8Unorm, 1)
        self.assertEqual(Metal.MTLPixelFormatR8Unorm, 10)
        self.assertEqual(Metal.MTLPixelFormatR8Unorm_sRGB, 11)
        self.assertEqual(Metal.MTLPixelFormatR8Snorm, 12)
        self.assertEqual(Metal.MTLPixelFormatR8Uint, 13)
        self.assertEqual(Metal.MTLPixelFormatR8Sint, 14)
        self.assertEqual(Metal.MTLPixelFormatR16Unorm, 20)
        self.assertEqual(Metal.MTLPixelFormatR16Snorm, 22)
        self.assertEqual(Metal.MTLPixelFormatR16Uint, 23)
        self.assertEqual(Metal.MTLPixelFormatR16Sint, 24)
        self.assertEqual(Metal.MTLPixelFormatR16Float, 25)
        self.assertEqual(Metal.MTLPixelFormatRG8Unorm, 30)
        self.assertEqual(Metal.MTLPixelFormatRG8Unorm_sRGB, 31)
        self.assertEqual(Metal.MTLPixelFormatRG8Snorm, 32)
        self.assertEqual(Metal.MTLPixelFormatRG8Uint, 33)
        self.assertEqual(Metal.MTLPixelFormatRG8Sint, 34)
        self.assertEqual(Metal.MTLPixelFormatB5G6R5Unorm, 40)
        self.assertEqual(Metal.MTLPixelFormatA1BGR5Unorm, 41)
        self.assertEqual(Metal.MTLPixelFormatABGR4Unorm, 42)
        self.assertEqual(Metal.MTLPixelFormatBGR5A1Unorm, 43)
        self.assertEqual(Metal.MTLPixelFormatR32Uint, 53)
        self.assertEqual(Metal.MTLPixelFormatR32Sint, 54)
        self.assertEqual(Metal.MTLPixelFormatR32Float, 55)
        self.assertEqual(Metal.MTLPixelFormatRG16Unorm, 60)
        self.assertEqual(Metal.MTLPixelFormatRG16Snorm, 62)
        self.assertEqual(Metal.MTLPixelFormatRG16Uint, 63)
        self.assertEqual(Metal.MTLPixelFormatRG16Sint, 64)
        self.assertEqual(Metal.MTLPixelFormatRG16Float, 65)
        self.assertEqual(Metal.MTLPixelFormatRGBA8Unorm, 70)
        self.assertEqual(Metal.MTLPixelFormatRGBA8Unorm_sRGB, 71)
        self.assertEqual(Metal.MTLPixelFormatRGBA8Snorm, 72)
        self.assertEqual(Metal.MTLPixelFormatRGBA8Uint, 73)
        self.assertEqual(Metal.MTLPixelFormatRGBA8Sint, 74)
        self.assertEqual(Metal.MTLPixelFormatBGRA8Unorm, 80)
        self.assertEqual(Metal.MTLPixelFormatBGRA8Unorm_sRGB, 81)
        self.assertEqual(Metal.MTLPixelFormatRGB10A2Unorm, 90)
        self.assertEqual(Metal.MTLPixelFormatRGB10A2Uint, 91)
        self.assertEqual(Metal.MTLPixelFormatRG11B10Float, 92)
        self.assertEqual(Metal.MTLPixelFormatRGB9E5Float, 93)
        self.assertEqual(Metal.MTLPixelFormatBGR10A2Unorm, 94)
        self.assertEqual(Metal.MTLPixelFormatBGR10_XR, 554)
        self.assertEqual(Metal.MTLPixelFormatBGR10_XR_sRGB, 555)
        self.assertEqual(Metal.MTLPixelFormatRG32Uint, 103)
        self.assertEqual(Metal.MTLPixelFormatRG32Sint, 104)
        self.assertEqual(Metal.MTLPixelFormatRG32Float, 105)
        self.assertEqual(Metal.MTLPixelFormatRGBA16Unorm, 110)
        self.assertEqual(Metal.MTLPixelFormatRGBA16Snorm, 112)
        self.assertEqual(Metal.MTLPixelFormatRGBA16Uint, 113)
        self.assertEqual(Metal.MTLPixelFormatRGBA16Sint, 114)
        self.assertEqual(Metal.MTLPixelFormatRGBA16Float, 115)
        self.assertEqual(Metal.MTLPixelFormatBGRA10_XR, 552)
        self.assertEqual(Metal.MTLPixelFormatBGRA10_XR_sRGB, 553)
        self.assertEqual(Metal.MTLPixelFormatRGBA32Uint, 123)
        self.assertEqual(Metal.MTLPixelFormatRGBA32Sint, 124)
        self.assertEqual(Metal.MTLPixelFormatRGBA32Float, 125)
        self.assertEqual(Metal.MTLPixelFormatBC1_RGBA, 130)
        self.assertEqual(Metal.MTLPixelFormatBC1_RGBA_sRGB, 131)
        self.assertEqual(Metal.MTLPixelFormatBC2_RGBA, 132)
        self.assertEqual(Metal.MTLPixelFormatBC2_RGBA_sRGB, 133)
        self.assertEqual(Metal.MTLPixelFormatBC3_RGBA, 134)
        self.assertEqual(Metal.MTLPixelFormatBC3_RGBA_sRGB, 135)
        self.assertEqual(Metal.MTLPixelFormatBC4_RUnorm, 140)
        self.assertEqual(Metal.MTLPixelFormatBC4_RSnorm, 141)
        self.assertEqual(Metal.MTLPixelFormatBC5_RGUnorm, 142)
        self.assertEqual(Metal.MTLPixelFormatBC5_RGSnorm, 143)
        self.assertEqual(Metal.MTLPixelFormatBC6H_RGBFloat, 150)
        self.assertEqual(Metal.MTLPixelFormatBC6H_RGBUfloat, 151)
        self.assertEqual(Metal.MTLPixelFormatBC7_RGBAUnorm, 152)
        self.assertEqual(Metal.MTLPixelFormatBC7_RGBAUnorm_sRGB, 153)
        self.assertEqual(Metal.MTLPixelFormatPVRTC_RGB_2BPP, 160)
        self.assertEqual(Metal.MTLPixelFormatPVRTC_RGB_2BPP_sRGB, 161)
        self.assertEqual(Metal.MTLPixelFormatPVRTC_RGB_4BPP, 162)
        self.assertEqual(Metal.MTLPixelFormatPVRTC_RGB_4BPP_sRGB, 163)
        self.assertEqual(Metal.MTLPixelFormatPVRTC_RGBA_2BPP, 164)
        self.assertEqual(Metal.MTLPixelFormatPVRTC_RGBA_2BPP_sRGB, 165)
        self.assertEqual(Metal.MTLPixelFormatPVRTC_RGBA_4BPP, 166)
        self.assertEqual(Metal.MTLPixelFormatPVRTC_RGBA_4BPP_sRGB, 167)
        self.assertEqual(Metal.MTLPixelFormatEAC_R11Unorm, 170)
        self.assertEqual(Metal.MTLPixelFormatEAC_R11Snorm, 172)
        self.assertEqual(Metal.MTLPixelFormatEAC_RG11Unorm, 174)
        self.assertEqual(Metal.MTLPixelFormatEAC_RG11Snorm, 176)
        self.assertEqual(Metal.MTLPixelFormatEAC_RGBA8, 178)
        self.assertEqual(Metal.MTLPixelFormatEAC_RGBA8_sRGB, 179)
        self.assertEqual(Metal.MTLPixelFormatETC2_RGB8, 180)
        self.assertEqual(Metal.MTLPixelFormatETC2_RGB8_sRGB, 181)
        self.assertEqual(Metal.MTLPixelFormatETC2_RGB8A1, 182)
        self.assertEqual(Metal.MTLPixelFormatETC2_RGB8A1_sRGB, 183)
        self.assertEqual(Metal.MTLPixelFormatASTC_4x4_sRGB, 186)
        self.assertEqual(Metal.MTLPixelFormatASTC_5x4_sRGB, 187)
        self.assertEqual(Metal.MTLPixelFormatASTC_5x5_sRGB, 188)
        self.assertEqual(Metal.MTLPixelFormatASTC_6x5_sRGB, 189)
        self.assertEqual(Metal.MTLPixelFormatASTC_6x6_sRGB, 190)
        self.assertEqual(Metal.MTLPixelFormatASTC_8x5_sRGB, 192)
        self.assertEqual(Metal.MTLPixelFormatASTC_8x6_sRGB, 193)
        self.assertEqual(Metal.MTLPixelFormatASTC_8x8_sRGB, 194)
        self.assertEqual(Metal.MTLPixelFormatASTC_10x5_sRGB, 195)
        self.assertEqual(Metal.MTLPixelFormatASTC_10x6_sRGB, 196)
        self.assertEqual(Metal.MTLPixelFormatASTC_10x8_sRGB, 197)
        self.assertEqual(Metal.MTLPixelFormatASTC_10x10_sRGB, 198)
        self.assertEqual(Metal.MTLPixelFormatASTC_12x10_sRGB, 199)
        self.assertEqual(Metal.MTLPixelFormatASTC_12x12_sRGB, 200)
        self.assertEqual(Metal.MTLPixelFormatASTC_4x4_LDR, 204)
        self.assertEqual(Metal.MTLPixelFormatASTC_5x4_LDR, 205)
        self.assertEqual(Metal.MTLPixelFormatASTC_5x5_LDR, 206)
        self.assertEqual(Metal.MTLPixelFormatASTC_6x5_LDR, 207)
        self.assertEqual(Metal.MTLPixelFormatASTC_6x6_LDR, 208)
        self.assertEqual(Metal.MTLPixelFormatASTC_8x5_LDR, 210)
        self.assertEqual(Metal.MTLPixelFormatASTC_8x6_LDR, 211)
        self.assertEqual(Metal.MTLPixelFormatASTC_8x8_LDR, 212)
        self.assertEqual(Metal.MTLPixelFormatASTC_10x5_LDR, 213)
        self.assertEqual(Metal.MTLPixelFormatASTC_10x6_LDR, 214)
        self.assertEqual(Metal.MTLPixelFormatASTC_10x8_LDR, 215)
        self.assertEqual(Metal.MTLPixelFormatASTC_10x10_LDR, 216)
        self.assertEqual(Metal.MTLPixelFormatASTC_12x10_LDR, 217)
        self.assertEqual(Metal.MTLPixelFormatASTC_12x12_LDR, 218)
        self.assertEqual(Metal.MTLPixelFormatBGRG422, 241)
        self.assertEqual(Metal.MTLPixelFormatDepth16Unorm, 250)
        self.assertEqual(Metal.MTLPixelFormatDepth32Float, 252)
        self.assertEqual(Metal.MTLPixelFormatStencil8, 253)
        self.assertEqual(Metal.MTLPixelFormatDepth24Unorm_Stencil8, 255)
        self.assertEqual(Metal.MTLPixelFormatDepth32Float_Stencil8, 260)
        self.assertEqual(Metal.MTLPixelFormatX32_Stencil8, 261)
        self.assertEqual(Metal.MTLPixelFormatX24_Stencil8, 262)
