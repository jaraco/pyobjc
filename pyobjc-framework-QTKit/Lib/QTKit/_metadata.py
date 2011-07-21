# Generated file, don't edit
# Source: BridgeSupport/QTKit.bridgesupport
# Last update: Thu Jul 21 08:55:53 2011

import objc, sys

if sys.maxint > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
    "QTTime": objc.createStructType('QTTime', sel32or64(b'{_QTTime="timeValue"q"timeScale"l"flags"l}', b'{_QTTime="timeValue"q"timeScale"q"flags"q}'), None),
    "QTTimeRange": objc.createStructType('QTTimeRange', sel32or64(b'{_QTTimeRange="time"{?="timeValue"q"timeScale"l"flags"l}"duration"{?="timeValue"q"timeScale"l"flags"l}}', b'{_QTTimeRange="time"{?="timeValue"q"timeScale"q"flags"q}"duration"{?="timeValue"q"timeScale"q"flags"q}}'), None),
}
constants = '''$QTAddImageCodecQuality$QTAddImageCodecType$QTCaptureConnectionAttributeDidChangeNotification$QTCaptureConnectionAttributeWillChangeNotification$QTCaptureConnectionAudioAveragePowerLevelsAttribute$QTCaptureConnectionAudioMasterVolumeAttribute$QTCaptureConnectionAudioPeakHoldLevelsAttribute$QTCaptureConnectionAudioVolumesAttribute$QTCaptureConnectionChangedAttributeKey$QTCaptureConnectionEnabledAudioChannelsAttribute$QTCaptureConnectionFormatDescriptionDidChangeNotification$QTCaptureConnectionFormatDescriptionWillChangeNotification$QTCaptureDeviceAVCTransportControlsAttribute$QTCaptureDeviceAVCTransportControlsPlaybackModeKey$QTCaptureDeviceAVCTransportControlsSpeedKey$QTCaptureDeviceAttributeDidChangeNotification$QTCaptureDeviceAttributeWillChangeNotification$QTCaptureDeviceAvailableInputSourcesAttribute$QTCaptureDeviceChangedAttributeKey$QTCaptureDeviceFormatDescriptionsDidChangeNotification$QTCaptureDeviceFormatDescriptionsWillChangeNotification$QTCaptureDeviceInputSourceIdentifierAttribute$QTCaptureDeviceInputSourceIdentifierKey$QTCaptureDeviceInputSourceLocalizedDisplayNameKey$QTCaptureDeviceLegacySequenceGrabberAttribute$QTCaptureDeviceLinkedDevicesAttribute$QTCaptureDeviceSuspendedAttribute$QTCaptureDeviceWasConnectedNotification$QTCaptureDeviceWasDisconnectedNotification$QTCaptureSessionErrorKey$QTCaptureSessionRuntimeErrorNotification$QTDataReferenceTypeFile$QTDataReferenceTypeHandle$QTDataReferenceTypePointer$QTDataReferenceTypeResource$QTDataReferenceTypeURL$QTErrorCaptureInputKey$QTErrorCaptureOutputKey$QTErrorDeviceKey$QTErrorExcludingDeviceKey$QTErrorRecordingSuccesfullyFinishedKey$QTFormatDescriptionAudioChannelLayoutAttribute$QTFormatDescriptionAudioMagicCookieAttribute$QTFormatDescriptionAudioStreamBasicDescriptionAttribute$QTFormatDescriptionVideoCleanApertureDisplaySizeAttribute$QTFormatDescriptionVideoEncodedPixelsSizeAttribute$QTFormatDescriptionVideoProductionApertureDisplaySizeAttribute$QTIndefiniteTime@{_QTTime=qll}$QTKitErrorDomain$QTMediaCharacteristicAudio$QTMediaCharacteristicCanSendVideo$QTMediaCharacteristicCanStep$QTMediaCharacteristicHasNoDuration$QTMediaCharacteristicHasSkinData$QTMediaCharacteristicHasVideoFrameRate$QTMediaCharacteristicNonLinear$QTMediaCharacteristicProvidesActions$QTMediaCharacteristicProvidesKeyFocus$QTMediaCharacteristicVisual$QTMediaCreationTimeAttribute$QTMediaDurationAttribute$QTMediaModificationTimeAttribute$QTMediaQualityAttribute$QTMediaSampleCountAttribute$QTMediaTimeScaleAttribute$QTMediaType3D$QTMediaTypeAttribute$QTMediaTypeBase$QTMediaTypeFlash$QTMediaTypeHint$QTMediaTypeMPEG$QTMediaTypeMovie$QTMediaTypeMusic$QTMediaTypeMuxed$QTMediaTypeQTVR$QTMediaTypeQuartzComposer$QTMediaTypeSkin$QTMediaTypeSound$QTMediaTypeSprite$QTMediaTypeStream$QTMediaTypeText$QTMediaTypeTimeCode$QTMediaTypeTween$QTMediaTypeVideo$QTMovieActiveSegmentAttribute$QTMovieApertureModeAttribute$QTMovieApertureModeClassic$QTMovieApertureModeClean$QTMovieApertureModeDidChangeNotification$QTMovieApertureModeEncodedPixels$QTMovieApertureModeProduction$QTMovieAskUnresolvedDataRefsAttribute$QTMovieAutoAlternatesAttribute$QTMovieChapterDidChangeNotification$QTMovieChapterListDidChangeNotification$QTMovieChapterName$QTMovieChapterStartTime$QTMovieChapterTargetTrackAttribute$QTMovieCloseWindowRequestNotification$QTMovieCopyrightAttribute$QTMovieCreationTimeAttribute$QTMovieCurrentSizeAttribute$QTMovieCurrentTimeAttribute$QTMovieDataAttribute$QTMovieDataReferenceAttribute$QTMovieDataSizeAttribute$QTMovieDelegateAttribute$QTMovieDidEndNotification$QTMovieDisplayNameAttribute$QTMovieDontInteractWithUserAttribute$QTMovieDurationAttribute$QTMovieEditabilityDidChangeNotification$QTMovieEditableAttribute$QTMovieEditedNotification$QTMovieEnterFullScreenRequestNotification$QTMovieExitFullScreenRequestNotification$QTMovieExport$QTMovieExportManufacturer$QTMovieExportSettings$QTMovieExportType$QTMovieFileNameAttribute$QTMovieFileOffsetAttribute$QTMovieFlatten$QTMovieFrameImageDeinterlaceFields$QTMovieFrameImageHighQuality$QTMovieFrameImageOpenGLContext$QTMovieFrameImagePixelFormat$QTMovieFrameImageRepresentationsType$QTMovieFrameImageSingleField$QTMovieFrameImageSize$QTMovieFrameImageType$QTMovieFrameImageTypeCGImageRef$QTMovieFrameImageTypeCIImage$QTMovieFrameImageTypeCVOpenGLTextureRef$QTMovieFrameImageTypeCVPixelBufferRef$QTMovieFrameImageTypeNSImage$QTMovieHasApertureModeDimensionsAttribute$QTMovieHasAudioAttribute$QTMovieHasDurationAttribute$QTMovieHasVideoAttribute$QTMovieIsActiveAttribute$QTMovieIsInteractiveAttribute$QTMovieIsLinearAttribute$QTMovieIsSteppableAttribute$QTMovieLoadStateAttribute$QTMovieLoadStateDidChangeNotification$QTMovieLoopModeDidChangeNotification$QTMovieLoopsAttribute$QTMovieLoopsBackAndForthAttribute$QTMovieMessageNotificationParameter$QTMovieMessageStringPostedNotification$QTMovieModificationTimeAttribute$QTMovieMutedAttribute$QTMovieNaturalSizeAttribute$QTMovieOpenAsyncOKAttribute$QTMoviePasteboardAttribute$QTMoviePasteboardType$QTMoviePlaysAllFramesAttribute$QTMoviePlaysSelectionOnlyAttribute$QTMoviePosterTimeAttribute$QTMoviePreferredMutedAttribute$QTMoviePreferredRateAttribute$QTMoviePreferredVolumeAttribute$QTMoviePreviewModeAttribute$QTMoviePreviewRangeAttribute$QTMovieRateAttribute$QTMovieRateChangesPreservePitchAttribute$QTMovieRateDidChangeNotification$QTMovieRateDidChangeNotificationParameter$QTMovieResolveDataRefsAttribute$QTMovieSelectionAttribute$QTMovieSelectionDidChangeNotification$QTMovieSizeDidChangeNotification$QTMovieStatusCodeNotificationParameter$QTMovieStatusFlagsNotificationParameter$QTMovieStatusStringNotificationParameter$QTMovieStatusStringPostedNotification$QTMovieTargetIDNotificationParameter$QTMovieTargetNameNotificationParameter$QTMovieTimeDidChangeNotification$QTMovieTimeScaleAttribute$QTMovieURLAttribute$QTMovieUneditableException$QTMovieViewControllerVisibleBinding$QTMovieViewFillColorBinding$QTMovieViewMovieBinding$QTMovieViewPreservesAspectRatioBinding$QTMovieVolumeAttribute$QTMovieVolumeDidChangeNotification$QTSampleBufferDateRecordedAttribute$QTSampleBufferExplicitSceneChange$QTSampleBufferHostTimeAttribute$QTSampleBufferSMPTETimeAttribute$QTSampleBufferSceneChangeTypeAttribute$QTSampleBufferTimeStampDiscontinuitySceneChange$QTTrackBoundsAttribute$QTTrackCreationTimeAttribute$QTTrackDimensionsAttribute$QTTrackDisplayNameAttribute$QTTrackEnabledAttribute$QTTrackFormatSummaryAttribute$QTTrackHasApertureModeDimensionsAttribute$QTTrackIDAttribute$QTTrackIsChapterTrackAttribute$QTTrackLayerAttribute$QTTrackMediaTypeAttribute$QTTrackModificationTimeAttribute$QTTrackRangeAttribute$QTTrackTimeScaleAttribute$QTTrackUsageInMovieAttribute$QTTrackUsageInPosterAttribute$QTTrackUsageInPreviewAttribute$QTTrackVolumeAttribute$QTZeroTime@{_QTTime=qll}$'''
enums = '''$AliasDataHandlerSubType@1634494835$BaseMediaType@1735291491$FlashMediaType@1718383464$HandleDataHandlerSubType@1752065132$MAC_OS_X_VERSION_10_4@1040$MAC_OS_X_VERSION_10_4@1040$MAC_OS_X_VERSION_10_5@1050$MAC_OS_X_VERSION_10_5@1050$MPEGMediaType@1297106247$MovieMediaType@1836019574$MusicMediaType@1836413801$NSINTEGER_DEFINED@1$NullDataHandlerSubType@1853189228$PointerDataHandlerSubType@1886679584$QTCaptureDeviceAVCTransportControlsFastForwardSpeed@13000$QTCaptureDeviceAVCTransportControlsFastReverseSpeed@-13000$QTCaptureDeviceAVCTransportControlsFastestForwardSpeed@19000$QTCaptureDeviceAVCTransportControlsFastestReverseSpeed@-19000$QTCaptureDeviceAVCTransportControlsNormalForwardSpeed@10000$QTCaptureDeviceAVCTransportControlsNormalReverseSpeed@-10000$QTCaptureDeviceAVCTransportControlsNotPlayingMode@0$QTCaptureDeviceAVCTransportControlsPlayingMode@1$QTCaptureDeviceAVCTransportControlsSlowForwardSpeed@7000$QTCaptureDeviceAVCTransportControlsSlowReverseSpeed@-7000$QTCaptureDeviceAVCTransportControlsSlowestForwardSpeed@1000$QTCaptureDeviceAVCTransportControlsSlowestReverseSpeed@-1000$QTCaptureDeviceAVCTransportControlsStoppedSpeed@0$QTCaptureDeviceAVCTransportControlsVeryFastForwardSpeed@16000$QTCaptureDeviceAVCTransportControlsVeryFastReverseSpeed@-16000$QTCaptureDeviceAVCTransportControlsVerySlowForwardSpeed@4000$QTCaptureDeviceAVCTransportControlsVerySlowReverseSpeed@-4000$QTCaptureFileOutputBufferDestinationNewFile@1$QTCaptureFileOutputBufferDestinationOldFile@2$QTErrorDeviceAlreadyUsedbyAnotherSession@1101$QTErrorDeviceExcludedByAnotherDevice@1302$QTErrorDeviceInUseByAnotherApplication@1301$QTErrorDeviceNotConnected@1300$QTErrorDeviceWasDisconnected@1203$QTErrorDiskFull@1202$QTErrorIncompatibleInput@1002$QTErrorIncompatibleOutput@1003$QTErrorInvalidInputsOrOutputs@1100$QTErrorMaximumDurationReached@1205$QTErrorMaximumFileSizeReached@1206$QTErrorMediaChanged@1204$QTErrorMediaDiscontinuity@1207$QTErrorNoDataCaptured@1200$QTErrorSessionConfigurationChanged@1201$QTErrorUnknown@-1$QTIncludeAggressiveTypes@4$QTIncludeAllTypes@65535$QTIncludeCommonTypes@0$QTIncludeDynamicTypes@8$QTIncludeStillImageTypes@1$QTIncludeTranslatableTypes@2$QTKIT_VERSION_7_0@70000$QTKIT_VERSION_7_2@70200$QTKIT_VERSION_MAX_ALLOWED@70200$QTKIT_VERSION_MIN_REQUIRED@70200$QTKIT_VERSION_MIN_REQUIRED@70200$QTMovieLoadStateComplete@100000$QTMovieLoadStateError@-1$QTMovieLoadStateLoaded@2000$QTMovieLoadStateLoading@1000$QTMovieLoadStatePlayable@10000$QTMovieLoadStatePlaythroughOK@20000$QTMovieOperationBeginPhase@0$QTMovieOperationBeginPhase@0$QTMovieOperationEndPhase@2$QTMovieOperationEndPhase@2$QTMovieOperationUpdatePercentPhase@1$QTMovieOperationUpdatePercentPhase@1$QTSampleBufferAudioBufferListOptionAssure16ByteAlignment@1$ResourceDataHandlerSubType@1920168547$SkinMediaType@1936419182$SoundMediaType@1936684398$SpriteMediaType@1936749172$TextMediaType@1952807028$ThreeDeeMediaType@1902392164$TimeCode64MediaType@1952658996$TimeCodeMediaType@1953325924$TweenMediaType@1953981806$URLDataHandlerSubType@1970433056$VideoMediaType@1986618469$WiredActionHandlerType@2003399269$codecHighQuality@768$codecLosslessQuality@1024$codecLowQuality@256$codecMaxQuality@1023$codecMinQuality@0$codecNormalQuality@512$graphicsModeComposition@259$graphicsModePerComponentAlpha@272$graphicsModePreBlackAlpha@258$graphicsModePreMulColorAlpha@261$graphicsModePreWhiteAlpha@257$graphicsModeStraightAlpha@256$graphicsModeStraightAlphaBlend@260$k16GrayCodecType@1647392359$k32AlphaGrayCodecType@1647522401$k422YpCbCr10CodecType@1983000880$k422YpCbCr16CodecType@1983000886$k422YpCbCr8CodecType@846624121$k4444YpCbCrA8CodecType@1983131704$k4444YpCbCrA8RCodecType@1916022840$k444YpCbCr10CodecType@1983131952$k444YpCbCr8CodecType@1983066168$k48RGBCodecType@1647589490$k64ARGBCodecType@1647719521$kAVRJPEGCodecType@1635152416$kAnimationCodecType@1919706400$kBMPCodecType@1465011269$kBaseCodecType@1650553701$kCMYKCodecType@1668118891$kCinepakCodecType@1668704612$kCloudCodecType@1668050805$kComponentVideoCodecType@2037741106$kComponentVideoSigned@2037741173$kComponentVideoUnsigned@2037741171$kDVCNTSCCodecType@1685480224$kDVCPALCodecType@1685480304$kDVCPROHD1080i50CodecType@1685481525$kDVCPROHD1080i60CodecType@1685481526$kDVCPROHD720pCodecType@1685481584$kDVCPro100NTSCCodecType@1685467502$kDVCPro100PALCodecType@1685467504$kDVCPro50NTSCCodecType@1685468526$kDVCPro50PALCodecType@1685468528$kDVCProPALCodecType@1685483632$kFLCCodecType@1718380899$kFireCodecType@1718186597$kGIFCodecType@1734960672$kGraphicsCodecType@1936548640$kH261CodecType@1748121137$kH263CodecType@1748121139$kH264CodecType@1635148593$kIndeo4CodecType@1230386225$kJPEG2000CodecType@1835692082$kJPEGCodecType@1785750887$kMPEG4VisualCodecType@1836070006$kMacPaintCodecType@1347310663$kMicrosoftVideo1CodecType@1836283491$kMotionJPEGACodecType@1835692129$kMotionJPEGBCodecType@1835692130$kMpegYUV420CodecType@1836676470$kOpenDMLJPEGCodecType@1684890161$kPNGCodecType@1886283552$kPhotoCDCodecType@1802527588$kPixletCodecType@1886940276$kPlanarRGBCodecType@943870035$kQTFileType3DMF@860114246$kQTFileType3GP2@862416946$kQTFileType3GPP@862417008$kQTFileTypeAIFC@1095321155$kQTFileTypeAIFF@1095321158$kQTFileTypeAMC@1634558752$kQTFileTypeAMR@1634562592$kQTFileTypeAVI@1449547552$kQTFileTypeAudioCDTrack@1953653099$kQTFileTypeBMP@1112363110$kQTFileTypeDVC@1685480225$kQTFileTypeFLC@1179403040$kQTFileTypeFlash@1398228556$kQTFileTypeFlashPix@1179675000$kQTFileTypeGIF@1195984486$kQTFileTypeJFIF@1246774599$kQTFileTypeJPEG@1246774599$kQTFileTypeJPEG2000@1785737760$kQTFileTypeMIDI@1298752617$kQTFileTypeMP4@1836082996$kQTFileTypeMacPaint@1347310663$kQTFileTypeMovie@1299148630$kQTFileTypeMuLaw@1431060823$kQTFileTypePDF@1346651680$kQTFileTypePICS@1346978643$kQTFileTypePNG@1347307366$kQTFileTypePhotoShop@943870035$kQTFileTypePicture@1346978644$kQTFileTypeQuickDrawGXPicture@1902405496$kQTFileTypeQuickTimeImage@1903454566$kQTFileTypeSDV@1935963680$kQTFileTypeSGIImage@777209673$kQTFileTypeSoundDesignerII@1399075430$kQTFileTypeSystemSevenSound@1936091500$kQTFileTypeTIFF@1414088262$kQTFileTypeTargaImage@1414547779$kQTFileTypeText@1413830740$kQTFileTypeWave@1463899717$kQTQuartzComposerMediaType@1903458848$kQTTimeIsIndefinite@1$kQuickDrawCodecType@1902408311$kQuickDrawGXCodecType@1902405496$kRawCodecType@1918990112$kSGICodecType@777209673$kSorenson3CodecType@1398165811$kSorensonCodecType@1398165809$kSorensonYUV9CodecType@1937339961$kTIFFCodecType@1953064550$kTargaCodecType@1952932128$kVectorCodecType@1885434984$kVideoCodecType@1919973985$kWaterRippleCodecType@1919512684$kWindowsRawCodecType@1465008471$kYUV420CodecType@2033463856$'''
misc.update({'NSIntegerMin': sel32or64(-2147483648, -9223372036854775808), 'NSIntegerMax': sel32or64(2147483647, 9223372036854775807), 'NSUIntegerMax': sel32or64(4294967295, 18446744073709551615L)})
misc.update({})
functions = {'QTStringForOSType': ('@L',), 'QTMakeTimeWithTimeRecord': (sel32or64('{_QTTime=qll}{TimeRecord={wide=Ii}i^{TimeBaseRecord}}', '{_QTTime=qqq}{TimeRecord={wide=Ii}i^{TimeBaseRecord}}'),), 'QTMakeTimeRange': (sel32or64('{_QTTimeRange={?=qll}{?=qll}}{_QTTime=qll}{_QTTime=qll}', '{_QTTimeRange={?=qqq}{?=qqq}}{_QTTime=qll}{_QTTime=qll}'),), 'QTStringFromTime': ('@{_QTTime=qll}',), 'QTTimeCompare': (sel32or64('i{_QTTime=qll}{_QTTime=qll}', 'q{_QTTime=qll}{_QTTime=qll}'),), 'QTTimeDecrement': (sel32or64('{_QTTime=qll}{_QTTime=qll}{_QTTime=qll}', '{_QTTime=qqq}{_QTTime=qll}{_QTTime=qll}'),), 'QTMakeTimeWithTimeInterval': (sel32or64('{_QTTime=qll}d', '{_QTTime=qqq}d'),), 'QTStringFromTimeRange': ('@{_QTTimeRange={?=qll}{?=qll}}',), 'QTOSTypeForString': (sel32or64('L@', 'I@'),), 'QTTimeRangeEnd': (sel32or64('{_QTTime=qll}{_QTTimeRange={?=qll}{?=qll}}', '{_QTTime=qqq}{_QTTimeRange={?=qll}{?=qll}}'),), 'QTTimeFromString': (sel32or64('{_QTTime=qll}@', '{_QTTime=qqq}@'),), 'QTGetTimeInterval': ('Z{_QTTime=qll}^d', '', {'arguments': {0: {'type': b'{_QTTime=qll}'}, 1: {'type': b'^d', 'type_modifier': b'o'}}}), 'QTTimeInTimeRange': ('Z{_QTTime=qll}{_QTTimeRange={?=qll}{?=qll}}',), 'QTUnionTimeRange': (sel32or64('{_QTTimeRange={?=qll}{?=qll}}{_QTTimeRange={?=qll}{?=qll}}{_QTTimeRange={?=qll}{?=qll}}', '{_QTTimeRange={?=qqq}{?=qqq}}{_QTTimeRange={?=qll}{?=qll}}{_QTTimeRange={?=qll}{?=qll}}'),), 'QTMakeTimeScaled': (sel32or64('{_QTTime=qll}{_QTTime=qll}l', '{_QTTime=qqq}{_QTTime=qll}l'),), 'QTTimeIncrement': (sel32or64('{_QTTime=qll}{_QTTime=qll}{_QTTime=qll}', '{_QTTime=qqq}{_QTTime=qll}{_QTTime=qll}'),), 'QTTimeIsIndefinite': ('Z{_QTTime=qll}',), 'QTStringFromSMPTETime': ('@{SMPTETime=ssIIIssss}',), 'QTMakeTime': (sel32or64('{_QTTime=qll}ql', '{_QTTime=qqq}ql'),), 'QTTimeRangeFromString': (sel32or64('{_QTTimeRange={?=qll}{?=qll}}@', '{_QTTimeRange={?=qqq}{?=qqq}}@'),), 'QTEqualTimeRanges': ('Z{_QTTimeRange={?=qll}{?=qll}}{_QTTimeRange={?=qll}{?=qll}}',), 'QTIntersectionTimeRange': (sel32or64('{_QTTimeRange={?=qll}{?=qll}}{_QTTimeRange={?=qll}{?=qll}}{_QTTimeRange={?=qll}{?=qll}}', '{_QTTimeRange={?=qqq}{?=qqq}}{_QTTimeRange={?=qll}{?=qll}}{_QTTimeRange={?=qll}{?=qll}}'),), 'QTGetTimeRecord': ('Z{_QTTime=qll}^{TimeRecord={wide=Ii}i^{TimeBaseRecord}}', '', {'arguments': {0: {'type': b'{_QTTime=qll}'}, 1: {'type': b'^{TimeRecord={wide=Ii}i^{TimeBaseRecord}}', 'type_modifier': b'o'}}})}
cftypes = []
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    pass
    r('NSObject', b'captureOutput:shouldChangeOutputFileAtURL:forConnections:dueToError:', {'retval': {'type': b'Z'}})
    r('NSObject', b'movie:linkToURL:', {'retval': {'type': b'Z'}})
    r('NSObject', b'movie:shouldContinueOperation:withPhase:atPercent:withAttributes:', {'retval': {'type': b'Z'}})
    r('NSObject', b'movieShouldLoadData:', {'retval': {'type': b'Z'}})
    r('NSObject', b'movieShouldTask:', {'retval': {'type': b'Z'}})
    r('QTCaptureConnection', b'attributeIsReadOnly:', {'retval': {'type': b'Z'}})
    r('QTCaptureConnection', b'isEnabled', {'retval': {'type': b'Z'}})
    r('QTCaptureConnection', b'setEnabled:', {'arguments': {2: {'type': b'Z'}}})
    r('QTCaptureDevice', b'attributeIsReadOnly:', {'retval': {'type': b'Z'}})
    r('QTCaptureDevice', b'hasMediaType:', {'retval': {'type': b'Z'}})
    r('QTCaptureDevice', b'isConnected', {'retval': {'type': b'Z'}})
    r('QTCaptureDevice', b'isInUseByAnotherApplication', {'retval': {'type': b'Z'}})
    r('QTCaptureDevice', b'isOpen', {'retval': {'type': b'Z'}})
    r('QTCaptureDevice', b'open:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type_modifier': b'o'}}})
    r('QTCaptureSession', b'addInput:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r('QTCaptureSession', b'addOutput:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r('QTCaptureSession', b'isRunning', {'retval': {'type': b'Z'}})
    r('QTCaptureView', b'preservesAspectRatio', {'retval': {'type': b'Z'}})
    r('QTCaptureView', b'setPreservesAspectRatio:', {'arguments': {2: {'type': b'Z'}}})
    r('QTCompressionOptions', b'isEqualToCompressionOptions:', {'retval': {'type': b'Z'}})
    r('QTDataReference', b'dataReferenceWithDataRef:type:', {'arguments': {2: {'type': b'^*'}}})
    r('QTDataReference', b'initWithDataRef:type:', {'arguments': {2: {'type': b'^*'}}})
    r('QTDataReference', b'setDataRef:', {'arguments': {2: {'type': b'^*'}}})
    r('QTFormatDescription', b'isEqualToFormatDescription:', {'retval': {'type': b'Z'}})
    r('QTMedia', b'hasCharacteristic:', {'retval': {'type': b'Z'}})
    r('QTMedia', b'initWithQuickTimeMedia:error:', {'arguments': {2: {'type': b'^^{MediaType}'}, 3: {'type_modifier': b'o'}}})
    r('QTMedia', b'mediaWithQuickTimeMedia:error:', {'arguments': {2: {'type': b'^^{MediaType}'}, 3: {'type_modifier': b'o'}}})
    r('QTMovie', b'frameImageAtTime:withAttributes:error:', {'arguments': {4: {'type_modifier': b'o'}}})
    r('QTMovie', b'initToWritableData:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r('QTMovie', b'addChapters:withAttributes:error:', {'arguments': {4: {'type_modifier': b'o'}}})
    r('QTMovie', b'attachToCurrentThread', {'retval': {'type': b'Z'}})
    r('QTMovie', b'canInitWithDataReference:', {'retval': {'type': b'Z'}})
    r('QTMovie', b'canInitWithFile:', {'retval': {'type': b'Z'}})
    r('QTMovie', b'canInitWithPasteboard:', {'retval': {'type': b'Z'}})
    r('QTMovie', b'canInitWithURL:', {'retval': {'type': b'Z'}})
    r('QTMovie', b'canUpdateMovieFile', {'retval': {'type': b'Z'}})
    r('QTMovie', b'detachFromCurrentThread', {'retval': {'type': b'Z'}})
    r('QTMovie', b'hasChapters', {'retval': {'type': b'Z'}})
    r('QTMovie', b'initToWritableDataReference:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r('QTMovie', b'initToWritableFile:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r('QTMovie', b'initWithAttributes:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r('QTMovie', b'initWithData:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r('QTMovie', b'initWithDataReference:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r('QTMovie', b'initWithFile:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r('QTMovie', b'initWithMovie:timeRange:error:', {'arguments': {4: {'type_modifier': b'o'}}})
    r('QTMovie', b'initWithPasteboard:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r('QTMovie', b'initWithQuickTimeMovie:disposeWhenDone:error:', {'arguments': {3: {'type': b'Z'}, 4: {'type_modifier': b'o'}}})
    r('QTMovie', b'initWithURL:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r('QTMovie', b'isIdling', {'retval': {'type': b'Z'}})
    r('QTMovie', b'movieNamed:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r('QTMovie', b'movieWithAttributes:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r('QTMovie', b'movieWithData:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r('QTMovie', b'movieWithDataReference:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r('QTMovie', b'movieWithFile:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r('QTMovie', b'movieWithPasteboard:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r('QTMovie', b'movieWithQuickTimeMovie:disposeWhenDone:error:', {'arguments': {3: {'type': b'Z'}, 4: {'type_modifier': b'o'}}})
    r('QTMovie', b'movieWithTimeRange:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r('QTMovie', b'movieWithURL:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r('QTMovie', b'muted', {'retval': {'type': b'Z'}})
    r('QTMovie', b'removeChapters', {'retval': {'type': b'Z'}})
    r('QTMovie', b'setIdling:', {'arguments': {2: {'type': b'Z'}}})
    r('QTMovie', b'setMuted:', {'arguments': {2: {'type': b'Z'}}})
    r('QTMovie', b'updateMovieFile', {'retval': {'type': b'Z'}})
    r('QTMovie', b'writeToFile:withAttributes:', {'retval': {'type': b'Z'}})
    r('QTMovie', b'writeToFile:withAttributes:error:', {'retval': {'type': b'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r('QTMovieView', b'areStepButtonsVisible', {'retval': {'type': b'Z'}})
    r('QTMovieView', b'areZoomButtonsVisible', {'retval': {'type': b'Z'}})
    r('QTMovieView', b'isBackButtonVisible', {'retval': {'type': b'Z'}})
    r('QTMovieView', b'isControllerVisible', {'retval': {'type': b'Z'}})
    r('QTMovieView', b'isCustomButtonVisible', {'retval': {'type': b'Z'}})
    r('QTMovieView', b'isEditable', {'retval': {'type': b'Z'}})
    r('QTMovieView', b'isHotSpotButtonVisible', {'retval': {'type': b'Z'}})
    r('QTMovieView', b'isTranslateButtonVisible', {'retval': {'type': b'Z'}})
    r('QTMovieView', b'isVolumeButtonVisible', {'retval': {'type': b'Z'}})
    r('QTMovieView', b'preservesAspectRatio', {'retval': {'type': b'Z'}})
    r('QTMovieView', b'setBackButtonVisible:', {'arguments': {2: {'type': b'Z'}}})
    r('QTMovieView', b'setControllerVisible:', {'arguments': {2: {'type': b'Z'}}})
    r('QTMovieView', b'setCustomButtonVisible:', {'arguments': {2: {'type': b'Z'}}})
    r('QTMovieView', b'setEditable:', {'arguments': {2: {'type': b'Z'}}})
    r('QTMovieView', b'setHotSpotButtonVisible:', {'arguments': {2: {'type': b'Z'}}})
    r('QTMovieView', b'setPreservesAspectRatio:', {'arguments': {2: {'type': b'Z'}}})
    r('QTMovieView', b'setShowsResizeIndicator:', {'arguments': {2: {'type': b'Z'}}})
    r('QTMovieView', b'setStepButtonsVisible:', {'arguments': {2: {'type': b'Z'}}})
    r('QTMovieView', b'setTranslateButtonVisible:', {'arguments': {2: {'type': b'Z'}}})
    r('QTMovieView', b'setVolumeButtonVisible:', {'arguments': {2: {'type': b'Z'}}})
    r('QTMovieView', b'setZoomButtonsVisible:', {'arguments': {2: {'type': b'Z'}}})
    r('QTSampleBuffer', b'getAudioStreamPacketDescriptions:inRange:', {'retval': {'type': b'Z'}})
    r('QTTrack', b'isEnabled', {'retval': {'type': b'Z'}})
    r('QTTrack', b'setEnabled:', {'arguments': {2: {'type': b'Z'}}})
finally:
    objc._updatingMetadata(False)
protocols={'QTCaptureVideoPreviewOutputDelegate': objc.informal_protocol('QTCaptureVideoPreviewOutputDelegate', [objc.selector(None, 'captureOutput:didOutputVideoFrame:withSampleBuffer:fromConnection:', 'v@:@^{__CVBuffer=}@@', isRequired=False)]), 'QTMovieViewDelegate': objc.informal_protocol('QTMovieViewDelegate', [objc.selector(None, 'view:willDisplayImage:', '@@:@@', isRequired=False)]), 'QTCaptureDecompressedVideoOutputDelegate': objc.informal_protocol('QTCaptureDecompressedVideoOutputDelegate', [objc.selector(None, 'captureOutput:didOutputVideoFrame:withSampleBuffer:fromConnection:', 'v@:@^{__CVBuffer=}@@', isRequired=False)]), 'QTCaptureFileOutputDelegate': objc.informal_protocol('QTCaptureFileOutputDelegate', [objc.selector(None, 'captureOutput:didFinishRecordingToOutputFileAtURL:forConnections:dueToError:', 'v@:@@@@', isRequired=False), objc.selector(None, 'captureOutput:didOutputSampleBuffer:fromConnection:', 'v@:@@@', isRequired=False), objc.selector(None, 'captureOutput:didStartRecordingToOutputFileAtURL:forConnections:', 'v@:@@@', isRequired=False), objc.selector(None, 'captureOutput:mustChangeOutputFileAtURL:forConnections:dueToError:', 'v@:@@@@', isRequired=False), objc.selector(None, 'captureOutput:shouldChangeOutputFileAtURL:forConnections:dueToError:', 'Z@:@@@@', isRequired=False), objc.selector(None, 'captureOutput:willFinishRecordingToOutputFileAtURL:forConnections:dueToError:', 'v@:@@@@', isRequired=False), objc.selector(None, 'captureOutput:willStartRecordingToOutputFileAtURL:forConnections:', 'v@:@@@', isRequired=False)]), 'QTMovieDelegate': objc.informal_protocol('QTMovieDelegate', [objc.selector(None, 'externalMovie:', '@@:@', isRequired=False), objc.selector(None, 'movie:linkToURL:', 'Z@:@@', isRequired=False), objc.selector(None, 'movie:shouldContinueOperation:withPhase:atPercent:withAttributes:', 'Z@:@@i@@', isRequired=False), objc.selector(None, 'movieShouldLoadData:', 'Z@:@', isRequired=False), objc.selector(None, 'movieShouldTask:', 'Z@:@', isRequired=False)]), 'QTCaptureViewDelegate': objc.informal_protocol('QTCaptureViewDelegate', [objc.selector(None, 'view:willDisplayImage:', '@@:@@', isRequired=False)])}
